import os
from common.file_utils import example_as_lines, input_as_lines


def part_1(input, number_of_iterations):
    groups = []
    distances = []
    for i in range(len(input)):
        to_plug = input[i]
        for j in range(len(input)):
            to_compare = input[j]
            distance = (to_plug[0] - to_compare[0])**2 + (to_plug[1] - to_compare[1])**2 + (to_plug[2] - to_compare[2])**2
            distances.append(distance)
    max_distance = max(distances)
    for i in range(len(input)):
        for j in range(i, len(input)):
            distances[i * len(input) + j] = max_distance + 1

    sorted_distances = sorted(distances)

    already_visited_pairs = [(i, i) for i in range(len(input))]
    for _ in range(number_of_iterations):
        min_distance = 0
        pair_i = -1
        pair_j = -1
        for i in range(len(distances)):
            for j in range(len(distances[i])):
                if (i, j) in already_visited_pairs:
                    continue
                distance = distances[i][j]
                if min_distance == 0 or distance < min_distance:
                    min_distance = distance
                    pair_i, pair_j = i, j
        already_visited_pairs.append((pair_i, pair_j))
        already_visited_pairs.append((pair_j, pair_i))

        print(pair_i, pair_j)
        i_group = []
        j_group = []
        for group in groups:
            if pair_i in group:
                i_group = group
                break
        for group in groups:
            if pair_j in group:
                j_group = group
                break

        if len(i_group) == len(j_group) == 0:
            groups.append([pair_i, pair_j])
            continue
        if i_group == j_group:
            continue

        if len(j_group) > 0 and len(i_group) > 0:
            new_group = list(set(j_group + i_group))
            groups = list(filter(lambda g: g != j_group and g != i_group, groups)) + [new_group]
        elif len(j_group) > 0:
            j_group.append(pair_i)
        elif len(i_group) > 0:
            i_group.append(pair_j)
    sorted_lengths = sorted(len(group) for group in groups)
    return sorted_lengths[-1] * sorted_lengths[-2] * sorted_lengths[-3]






def part_2(input):
    pass


def process_input(input):
    return [list(map(lambda x: int(x), line.split(','))) for line in input]


if __name__ == '__main__':
    parent_folder = os.path.basename(os.path.dirname(__file__))
    example = example_as_lines(parent_folder)
    input = input_as_lines(parent_folder)

    print("example part_1")
    print(part_1(process_input(example), 10))
    print("input part_1")
    print(part_1(process_input(input), 1000))

    print("example part_2")
    print(part_2(process_input(example)))
    print("input part_2")
    print(part_2(process_input(input)))
