from enum import Enum
from .mapper import GolemMapper
from .nodeagent import NodeAgent
from typing import List,Dict,Any
import json
from yapapi import Task

class Operator(Enum):
    MAP = 1
    MAP_VALUES = 2
    FILTER = 3
    SAVE_CACHE = 4
    LOAD_CACHE = 5
    GROUP_BY_KEY = 6
    COUNT = 7
    COLLECT = 8
    REDUCE = 9



class Func:
    op: Operator
    func_literal: str

class GolemMapRunner:
    ''' This will run on a Golem node using a requester.'''
    def __init__(self, tar_fname ,imports: List['str'], data: List[Any]):
        self.nodeagent: NodeAgent = NodeAgent(tar_fname, data, imports, self.step)
        self.nodeagent.start()
    
    def request(self, Func):
        self.current_request

    def step(self):
        # evaluate imports.
        for i in self.imports:
            eval(i)
        if op == Operator.SAVE_CACHE:
            self.mapper.cache()
        elif op == Operator.LOAD_CACHE:
            self.mapper.load_cache(int(operand))
        elif op == Operator.MAP:
            self.mapper.map(eval(operand))
        elif op == Operator.MAP_VALUES:
            self.mapper.mapValues(eval(operand))
        elif op == Operator.GROUP_BY_KEY:
            self.mapper.mapValues(eval(operand))
        elif op == Operator.FILTER:
            self.mapper.filter(eval(operand))
        elif op == Operator.COUNT:
            self.mapper.count()
        elif op == Operator.COLLECT:
            self.mapper.collect()