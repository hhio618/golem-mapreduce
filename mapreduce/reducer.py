import os
import yaml
from typing import List, Any
import json



class GolemMapper:
    def __init__(self, data: List[Any]):
        self.current = data

    def sync(self):
        json.dump(self.current, "/golem/work/current.json")
        json.dump(len(self.current), "/golem/work/len.json")

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
        self.current = filter(filterer, self.current)

    def count(self):
        return len(self.current)

    def collect(self):
        return len(self.current)

    def cache(self):
        self.cache.append(current.copy())

    def load_cache(self, idx):
        self.current = self.cache[idx]

    def pick_result(self):
        self.result.append(self.current.copy())