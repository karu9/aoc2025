import os
from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    cursor = 50
    num_0 = 0
    for i in range(len(input)):
        direction = 1 if input[i][0] == 'R' else -1
        num = int(input[i][1:])
        cursor = (cursor + (direction * num)) % 100
        if cursor == 0:
            num_0 += 1
    return num_0


def part_2(input):
    cursor = 50
    num_0 = 0
    for i in range(len(input)):
        previous_cursor = cursor
        direction = 1 if input[i][0] == 'R' else -1
        num = int(input[i][1:])
        raw_cursor = (cursor + (direction * num))
        cursor = raw_cursor % 100

        min_boundary = -100 if previous_cursor == 0 else 0
        max_boundary = 100
        has_ticked =  max_boundary <= raw_cursor  or raw_cursor <= min_boundary

        if has_ticked:
            if raw_cursor <= min_boundary:
                number_of_ticks = (-(raw_cursor - min_boundary) // 100) + 1
            if raw_cursor >= max_boundary:
                number_of_ticks = ((raw_cursor - max_boundary) // 100) + 1
            num_0 += number_of_ticks

    return num_0


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
