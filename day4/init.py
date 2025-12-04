import os
from typing import final

from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    final_count = 0
    length = len(input)
    width = len(input[0])
    output = [row.copy() for row in input]
    for i in range(1, length - 1):
        for j in range(1, width - 1):
            if input[i][j] != 1:
                continue
            count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    if input[i + di][j + dj] == 1:
                        count += 1
            if count < 4:
                final_count += 1
                output[i][j] = 0
    return final_count, output


def part_2(input):
    total_roll = sum([sum(row) for row in input])
    final_count, next_input = part_1(input)
    next_total_roll = sum([sum(row) for row in next_input])
    total = final_count
    while next_total_roll != total_roll:
        final_count, next_input = part_1(next_input)
        total_roll = next_total_roll
        next_total_roll = sum([sum(row) for row in next_input])
        total += final_count
    return total


def process_input(input):
    output = []
    output.append([0] * (len(input[0]) + 2))
    for line in input:
        output.append([0] + [1 if char == '@' else 0 for char in list(line)] + [0])
    output.append([0] * (len(input[0]) + 2))
    return output


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
