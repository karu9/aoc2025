import os.path
from os import getcwd


def input_as_lines(day: str) -> [str]:
    inp = f"{os.path.dirname(getcwd())}/{day}/input/input.txt"
    f = open(inp, "r")
    return list(map(lambda k: k[:-1], f.readlines()))


def example_as_lines(day: str) -> [str]:
    inp = f"{os.path.dirname(getcwd())}/{day}/input/example.txt"
    f = open(inp, "r")
    return list(map(lambda k: k[:-1], f.readlines()))
