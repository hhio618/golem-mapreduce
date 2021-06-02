from functools import reduce

class GolemMapReduceContext:
    def __init__(self, current):
        self.cache = []
        self.current = current

    def get_current(self):
        return self.current

    def set_current(self, current):
        self.current
    
    def map(self, mapper):
        map(mapper, self.current)
    
    def mapValues(self, mapper):
        map(lambda x: (x[0], mapper(x[1])), self.current)

    def reduce(self, reducer):
        reduce(reducer, self.current)

    def reduceByKey(self, reducer):
        reduce(reducer, self.current)

    def cache(self):
        self.cache = current.copy()