from functools import reduce
from itertools import groupby
from collections import defaultdict


class GolemMapReduceContext:
    def __init__(self, current):
        self.cache = []
        self.current = current

    def get_current(self):
        return self.current

    def set_current(self, current):
        self.current

    def flatMap(self, mapper):
        self.current = [y for y in mapper(x) for x in self.current]
    
    def map(self, mapper):
        map(mapper, self.current)
    
    def mapValues(self, mapper):
        map(lambda x: (x[0], mapper(x[1])), self.current)

    def reduce(self, reducer):
        reduce(reducer, self.current)

    def reduceByKey(self, reducer):
        reduce(reducer, self.current)

    def groupByKey(self):
        v = defaultdict(list)
        for key, value in sorted(self.current.items()):
            v[value].append(key)
        self.current = v.items()

    def distinct(self):
        self.current = list(set(self.current))

    def filter(self, filterer):
        filter(filterer, self.current)

    def count(self):
        return len(self.current)

    def cache(self):
        self.cache = current.copy()