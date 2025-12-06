import math
import os
import re

from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    return sum([line[1](line[0]) for line in input])


def part_2(input):
    return part_1(input)


def process_input(input):
    ops = []
    parsed_input = [(list(filter(None, re.split(r'\s+', line)))) for line in input]
    for i in range(len(parsed_input[0])):
        numbers = []
        for line in parsed_input:
            if line[i] == "+":
                ops.append((numbers, sum))
            elif line[i] == "*":
                ops.append((numbers, math.prod))
            else:
                numbers.append(int(line[i]))
    return ops

def process_input_2(input):
    ranges = []
    operators_line = input[-1]
    max_line_length = max([len(line) for line in input])
    last_operator = 0
    operators = []
    start_current_range = 0
    for i in range(0, max_line_length):
        if i > len(operators_line) - 1:
            ranges.append((last_operator, max_line_length + 1))
            break
        if operators_line[i] != " ":
            operators.append(sum if operators_line[i] == "+" else math.prod)
            if i == 0:
              continue
            ranges.append((last_operator, i - 1))
            last_operator = i
    all_nums_as_string = []
    for range_index in range(len(ranges)):
        nums_as_string = []
        for line in input[:-1]:
            rang = ranges[range_index]
            num_as_string = line[rang[0]:rang[1]]
            nums_as_string.append(num_as_string)
        all_nums_as_string.append(nums_as_string)
    all_nums = []
    for nums_as_string in all_nums_as_string:
        max_num_length = max([len(num) for num in nums_as_string])
        new_nums = []
        while max_num_length != 0:
            nums = ''.join([num[max_num_length-1] for num in nums_as_string if len(num) >= max_num_length])
            new_nums.append(int(''.join(nums)))
            max_num_length -= 1
        all_nums.append(new_nums)

    ops = []
    for i in range(len(operators)):
        ops.append((all_nums[i], operators[i]))
    return ops


if __name__ == '__main__':
    parent_folder = os.path.basename(os.path.dirname(__file__))
    example = example_as_lines(parent_folder)
    input = input_as_lines(parent_folder)

    print("example part_1")
    print(part_1(process_input(example)))
    print("input part_1")
    print(part_1(process_input(input)))

    print("example part_2")
    print(part_2(process_input_2(example)))
    print("input part_2")
    print(part_2(process_input_2(input)))
