#!/usr/bin/env python3
import argparse
import asyncio
import subprocess
import os
import pathlib
import sys
import argparse
import time
from typing import List

import yapapi
from yapapi.log import enable_default_logger, log_summary, log_event_repr  # noqa
from yapapi.package import vm
from yapapi import Executor, Task, WorkContext
from yapapi.rest.activity import BatchTimeoutError
from datetime import timedelta
from .utils import get_temp_log_file
from . import IMAGE
import logging

logger = logging.getLogger('pipeline')


class StepState:
    PENDING = "pending"
    SUCCESS = "success"
    ERROR = "error"


class NodeAgent:
    def __init__(self, tar_fname, data, imports, task_generator, verbose=False):
        """ Creates a new runner on top of Golem.network
            params:
                tar_fname: tar file to be sent to golem vm.
                data: data file to send.
                imports: python imports.
                task_generator: will be used to generate tasks for each map function.
        """
        self.verbose = verbose
        self.tar_fname = tar_fname
        self.data = data
        self.imports = imports
        self.task_generator = task_generator
  
    def start(self):
        """ Run through steps in parallel. """
        enable_default_logger()
        loop = asyncio.get_event_loop()
        task = loop.create_task(self.run_step(step))
        try:
            asyncio.get_event_loop().run_until_complete(task)
        except (Exception, KeyboardInterrupt) as e:
            logger.error(e)
            task.cancel()
            asyncio.get_event_loop().run_until_complete(task)


    async def run(self, timeout=timedelta(minutes=10), budget=10, subnet_tag="community.3" ):
        package = await vm.repo(
            image_hash=IMAGE,
            min_mem_gib=1,
            min_storage_gib=5.0,
        )
        async def worker(ctx: WorkContext, tasks):
            async for task in tasks:
                print(f"\033[36;1mSending the context zip file: {self.tar_fname}\033[0m")
                ctx.send_file(self.tar_fname , "/golem/work/context.zip")
                ctx.send_json(self.imports, "/golem/work/imports.json")
                ctx.send_json(self.data, "/golem/work/current.json")
                ctx.send_json({"operator": task.operator, "operand": task.operand}, "/golem/work/func.json")
                # extracting tar file.
                print(f"\033[36;1mExtracting the zip file: {self.tar_fname}\033[0m")
                ctx.run("/bin/sh", "-c", "unzip /golem/work/context.zip")
                
                command = f"/golem/work/main.py"
                print(f"\033[36;1mRunning {command}\033[0m")
                ctx.run("/bin/sh", "-c", f"{command} >> /golem/output/cmd.log 2>&1")
                log_fname = get_temp_log_file(step_name)
                ctx.download_file(f"/golem/output/cmd.log", log_fname)
                try:
                    yield ctx.commit(timeout=timedelta(minutes=30))
                    task.accept_result(result=log_fname)
                except BatchTimeoutError:
                    print(f"Task timed out: {task}, time: {task.running_time}")
                    raise
            ctx.log("no more task to run")

        # By passing `event_emitter=log_summary()` we enable summary logging.
        # See the documentation of the `yapapi.log` module on how to set
        # the level of detail and format of the logged information.
        async with Executor(
            package=package,
            max_workers=1,
            budget=budget,
            timeout=timeout,
            subnet_tag=subnet_tag,
            event_consumer=log_summary(log_event_repr),
        ) as executer:
            async for task in executer.submit(worker, [self.task_generator]):
                print(f"\033[36;1mStep completed: {task}\033[0m")
                # # grab the logs
                # self.state[step['name']]['log'] = task.result
                # # notify about this task!
                # self.state[step['name']]['state'] = StepState.SUCCESS
                # self.post_progress(step['name'])
