import os
from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    fresh_ranges, availables = input
    count = 0
    for available in availables:
        for fresh_range in fresh_ranges:
            if available in fresh_range:
                count += 1
                break
    return count

def part_2(input):
    fresh_ranges, availables = input

    def join_ranges(ranges):
        final_ranges = []
        ignore_ranges = []
        for i in range(0, len(ranges)):
            if i in ignore_ranges:
                continue
            break_flag = False
            range_a = ranges[i]
            for j in range(i + 1, len(ranges)):
                range_b = ranges[j]
                if not (range_a.stop < range_b.start or range_b.stop < range_a.start):
                    new_range = range(min(range_a.start, range_b.start), max(range_a.stop, range_b.stop))
                    final_ranges.append(new_range)
                    break_flag = True
                    ignore_ranges.append(j)
                    break
            if break_flag:
                continue
            final_ranges.append(range_a)
        return final_ranges

    new_ranges = join_ranges(fresh_ranges)
    while new_ranges != fresh_ranges:
        fresh_ranges = new_ranges
        new_ranges = join_ranges(fresh_ranges)

    return sum(len(rang) for rang in new_ranges)


def process_input(input):
    fresh_ranges = []
    available = []
    pivot = False
    for line in input:
        if len(line) == 0:
            pivot = True
            continue
        if not pivot:
            ranges = line.split('-')
            fresh_ranges.append(range(int(ranges[0]), int(ranges[1]) + 1))
        if pivot:
            available.append(int(line))
    return fresh_ranges, available



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
