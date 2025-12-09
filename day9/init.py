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

def lines_intersect(rectangle_edge, input_edge, rectangle_edge_direction, side):
    if rectangle_edge_direction[0] == 0:
        x = rectangle_edge[0][0]
        ys = [rectangle_edge[0][1], rectangle_edge[1][1]]
        min_y = min(ys)
        max_y = max(ys)
        input_y = input_edge[0][1]
        input_xs = [input_edge[0][0], input_edge[1][0]]
        min_input_x = min(input_xs)
        max_input_x = max(input_xs)
        if min_input_x > x or max_input_x < x:
            return False
        if min_y > input_y or max_y < input_y:
            return False
        if (x == min_input_x or x == max_input_x) and (input_y == min_y or input_y == max_y):
            return False
        if side == 'left' and x < max_input_x or side == 'right' and x > min_input_x:
            return True
        return False
    else:
        y = rectangle_edge[0][1]
        xs = [rectangle_edge[0][0], rectangle_edge[1][0]]
        min_x = min(xs)
        max_x = max(xs)
        input_x = input_edge[0][0]
        input_ys = [input_edge[0][1], input_edge[1][1]]
        min_input_y = min(input_ys)
        max_input_y = max(input_ys)
        if min_input_y > y or max_input_y < y:
            return False
        if min_x > input_x or max_x < input_x:
            return False
        if (y == min_input_y or y == max_input_y) and (input_x == min_x or input_x == max_x):
            return False
        if side == 'top' and y < max_input_y or side == 'bottom' and y > min_input_y:
            return True
        return False


def filter_edges(edgs, min_x, max_x, min_y, max_y):
    filtered_edges = []
    for edge in edgs:
        edge_xs = [edge[0][0], edge[1][0]]
        edge_ys = [edge[0][1], edge[1][1]]
        if max(edge_xs) < min_x or min(edge_xs) > max_x or max(edge_ys) < min_y or min(edge_ys) > max_y:
            continue
        filtered_edges.append(edge)
    return filtered_edges

def rectangle_inside(i_point, j_point, edgs):
    min_x = min(i_point[0], j_point[0])
    max_x = max(i_point[0], j_point[0])
    min_y = min(i_point[1], j_point[1])
    max_y = max(i_point[1], j_point[1])
    if min_y == max_y or min_x == max_x:
        return False
    filtered_edges = filter_edges(edgs, min_x, max_x, min_y, max_y)
    boundaries = [[min_x, min_y], [min_x, max_y], [max_x, max_y], [max_x, min_y]]
    sides = ['left', 'bottom', 'right', 'top']
    for i in range(len(boundaries)):
        rectangle_edge = (boundaries[i], boundaries[(i+1) % len(boundaries)])
        side = sides[i]
        rectangle_edge_direction = (rectangle_edge[1][0] - rectangle_edge[0][0], rectangle_edge[1][1] - rectangle_edge[0][1])
        for input_edge in filtered_edges:
            input_edge_direction = (input_edge[1][0] - input_edge[0][0], input_edge[1][1] - input_edge[0][1])
            cross_product = rectangle_edge_direction[0] * input_edge_direction[1] - rectangle_edge_direction[1] * input_edge_direction[0]
            if cross_product == 0:
                # don't check for parallel lines
                continue
            if lines_intersect(rectangle_edge, input_edge, rectangle_edge_direction, side):
                return False
    return True

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
