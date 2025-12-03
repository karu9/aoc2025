import os
from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    sum = 0
    for line in input:
        max = 0
        max_index = 0
        for i in line:
            if int(i) > max and line.index(i) != len(line) - 1:
                max = int(i)
                max_index = line.index(i)
        second_max = 0
        for j in range(max_index + 1, len(line)):
            if int(line[j]) > second_max:
                second_max = int(line[j])
        sum += max * 10 + second_max
    return sum


def part_2(input):
    sum = 0
    for line in input:
        numbers = [int(i) for i in line]
        num_digits = 12
        min_index = 0
        final_joltage = []
        while num_digits > 0:
            segment = numbers[min_index : len(numbers) - num_digits + 1]
            print(segment)
            max_digit = max(segment)
            min_index = min_index + segment.index(max_digit) + 1
            num_digits -= 1
            final_joltage.append(max_digit)
        sum += int(''.join([str(i) for i in final_joltage]))
    return sum


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
