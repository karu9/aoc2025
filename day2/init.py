import os
from re import split

from common.file_utils import example_as_lines, input_as_lines

def isValid(id):
    if len(id) % 2 == 1:
        return True
    first_half = id[:len(id)//2]
    second_half = id[len(id)//2:]
    return first_half != second_half

def isValid_part_2(id):
    buffer_size = 1
    while buffer_size <= len(id) // 2:
        if len(id) % buffer_size == 0:
            sequence = id[:buffer_size]
            repetitions = len(id) // buffer_size
            if sequence * repetitions == id:
                return False
        buffer_size += 1
    return True

def get_all_ids(input):
    all_ids = []
    for rang in input:
        start = int(rang[0])
        end = int(rang[1])
        for id in range(start, end + 1):
            all_ids.append(str(id))
    return all_ids

def part_1(input):
    all_ids = get_all_ids(input)
    invalid_ids = []
    for id in all_ids:
        if not isValid(id):
            invalid_ids.append(id)
    return sum([int(id) for id in invalid_ids])

def part_2(input):
    all_ids = get_all_ids(input)
    invalid_ids = []
    for id in all_ids:
        if not isValid_part_2(id):
            invalid_ids.append(id)
    return sum([int(id) for id in invalid_ids])


def process_input(input):
    return [split('-', rang) for rang in split(',', input[0])]


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
