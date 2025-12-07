import os
from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    max_x, max_y, start_coords, beam_coords = input
    curr_xs = [start_coords[0]]
    curr_y = 1
    count = 0
    while beam_coords.get(curr_y, None) is not None:
        beam_xs = beam_coords[curr_y]
        intersect = list(set(curr_xs).intersection(beam_xs))
        count += len(intersect)
        curr_xs = list(set([i+1 for i in intersect] + [i-1 for i in intersect] + list(set(curr_xs).difference(beam_xs))))
        curr_y += 1
    return count


def part_2(input):
    max_x, max_y, start_coords, beam_coords = input
    curr_xs = {start_coords[0]: 1}
    curr_y = 1
    while beam_coords.get(curr_y, None) is not None:
        beam_xs = beam_coords[curr_y]
        for x in beam_xs:
            if curr_xs.get(x, None) is not None:
                count = curr_xs[x]
                del curr_xs[x]
                curr_xs[x + 1] = curr_xs.get(x + 1, 0) + count
                curr_xs[x - 1] = curr_xs.get(x - 1, 0) + count
        curr_y += 1
    return sum(curr_xs.values())


def process_input(input):
    start_coords = []
    beam_coords = {}
    max_y = len(input) // 2
    max_x = len(input[0])
    for jj in range(0, len(input), 2):

        line = input[jj]
        j = jj // 2
        if "S" in line:
            start_coords = (line.index("S"), j)
            continue

        beam_coords_j = []
        for i in range(len(input[0])):
            if line[i] == "^":
                beam_coords_j.append(i)
        beam_coords[j] = beam_coords_j
    return max_x, max_y, start_coords, beam_coords




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
