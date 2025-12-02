import functools
import os
from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    return functools.reduce(lambda acc, val: (acc[0]+1 if (acc[1] + {'R': 1, 'L': -1}[val[0]]*int(val[1:])) % 100 == 0 else acc[0], (acc[1] + {'R': 1, 'L': -1}[val[0]]*int(val[1:])) % 100), input, (0, 50))[0]


def part_2(input):
    pass


def process_input(input):
    return input


if __name__ == '__main__':
    parent_folder = os.path.basename(os.path.dirname(__file__))
    example = example_as_lines(parent_folder)
    input = input_as_lines(parent_folder)

    print("example part_1")
    print(part_1(process_input(example)))
    print("input part_1")
    print(part_1(process_input(input)))

    print("example part_2")
    print(part_2(process_input(example)))
    print("input part_2")
    print(part_2(process_input(input)))
