from enum import Enum
from .mapper import GolemMapper
from golem_mapreduce.runner import Operator,Func
import json


if __name__ == '__main__':
    mapper: GolemMapper = GolemMapper(json.load("/golem/work/current.json"))
    func = json.load("/golem/work/func.json")
    imports = json.load("/golem/work/imports.json")
    op, operand = func["operator"], func["operand"]
    for i in imports:
        exec(i)
    if op == Operator.SAVE_CACHE:
        mapper.cache()
    elif op == Operator.LOAD_CACHE:
        mapper.load_cache(int(operand))
    elif op == Operator.MAP:
        mapper.map(eval(operand))
    elif op == Operator.MAP_VALUES:
        mapper.mapValues(eval(operand))
    elif op == Operator.GROUP_BY_KEY:
        mapper.mapValues(eval(operand))
    elif op == Operator.FILTER:
        mapper.filter(eval(operand))
    elif op == Operator.COUNT:
        # needs to download len.json.
        pass
    elif op == Operator.COLLECT:
        # needs to download current.json.
        pass
    sync()