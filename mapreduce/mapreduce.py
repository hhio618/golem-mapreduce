import os
import yaml
from .context import GolemMapReduceContext


class MapReducer:
    def __init__(self, context: GolemMapReduceContext):
        self.context = context
    
    def map(mapper):
        self.context.map(mapper)
    
    def mapValues(mapper):
        self.context.mapValues(mapper)
    
    def reduce(reducer):
        self.context.reduce(reducer)
        