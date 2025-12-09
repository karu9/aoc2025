import os
from common.file_utils import example_as_lines, input_as_lines


def part_1(input):
    maxes = []
    for i in range(len(input)):
        i_point = input[i]
        for j in range(i+1, len(input)):
            j_point = input[j]
            maxes.append((abs(i_point[0] - j_point[0]) +1) * (abs(i_point[1] - j_point[1]) + 1))
    return max(maxes)



def edges(points):
    edges = []
    for i in range(len(points)):
        i_point = points[i]
        j_point = points[(i+1) % len(points)]
        edges.append((i_point, j_point))
    return edges

def has_edges_with_points_inside(edgs, min_x, max_x, min_y, max_y):

    for edge in edgs:
        edge_xs = [edge[0][0], edge[1][0]]
        edge_ys = [edge[0][1], edge[1][1]]
        min_edge_x = min(edge_xs)
        max_edge_x = max(edge_xs)
        min_edge_y = min(edge_ys)
        max_edge_y = max(edge_ys)
        if max_edge_y <= min_y or min_edge_y >= max_y or max_edge_x <= min_x or min_edge_x >= max_x:
            continue
        return True

    return False

def rectangle_inside(i_point, j_point, edgs):
    min_x = min(i_point[0], j_point[0])
    max_x = max(i_point[0], j_point[0])
    min_y = min(i_point[1], j_point[1])
    max_y = max(i_point[1], j_point[1])
    if min_y == max_y or min_x == max_x:
        return False
    return not has_edges_with_points_inside(edgs, min_x, max_x, min_y, max_y)


def part_2(input):
    maxes = []
    edgs = edges(input)
    for i in range(len(input)):
        i_point = input[i]
        for j in range(i + 1, len(input)):
            j_point = input[j]
            if not rectangle_inside(i_point, j_point, edgs):
                continue
            maxes.append((abs(i_point[0] - j_point[0]) + 1) * (abs(i_point[1] - j_point[1]) + 1))
    return max(maxes)


def process_input(input):
    return [list(map(lambda x: int(x), line.split(','))) for line in input]


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
