from functools import reduce
from itertools import groupby
from collections import defaultdict
from .runner import Runner


class NodeNotInitedError(Exception):
    pass

class GolemMapReduceContext:
    ''' Local context for running the Map Reduce programming model on top of 
        Golem.network.
    '''
    def __init__(self, current):
        self.cache = []
        self.current = current
        self.wait_for_stream = True
        self.node_inited = False
        # TODO: create tar from user code somehow!
        self.node_runner = Runner(tar_fname)
    

    def on_node_init(self, node_id):
        self.node_id = node_id
        self.current = filter(lambda x: x[0] == node_id, self.current)

    def get_current(self):
        return self.current

    def set_current(self, current):
        self.current
