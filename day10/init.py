import math
import os
from random import randint

from common.file_utils import example_as_lines, input_as_lines




def part_1(input):
    number_of_tries = []

    for line in input:
        current_record = []

        def push_buttons(expected_state, buttons, pressed_buttons, previous_states):
            if len(current_record) > 0 and len(pressed_buttons) >= current_record[0]:
                return
            previous_button = pressed_buttons[-1] if len(pressed_buttons) > 0 else None
            all_buttons_to_push = [i for i in range(len(buttons)) if i != previous_button]
            for i in all_buttons_to_push:
                current_button = buttons[i]
                previous_state = previous_states[-1]
                next_state = [not previous_state[i] if i in current_button else previous_state[i] for i in range(len(previous_state))]
                if next_state in previous_states:
                    return
                if next_state == expected_state:
                    if len(current_record) == 0 :
                        current_record.append(len(pressed_buttons) + 1)
                    else:
                        current_record[0] = len(pressed_buttons) + 1
                push_buttons(expected_state, buttons, pressed_buttons + [current_button], previous_states + [next_state])


        push_buttons(line[0], line[1], [], [[False for i in range(len(line[0]))]])
        number_of_tries.append(current_record[0])
    return sum(number_of_tries)



def part_2(input):
    number_of_tries = []

    for line in input:
        joltages = line[2]
        sum_of_joltages = sum(joltages)
        current_record = [sum_of_joltages]

        def push_buttons(expected_state, button_masks, count, previous_state, blacklist):
            if count >= current_record[0]:
                return

            next_states = []
            next_blacklist = blacklist.copy()
            for i in range(len(button_masks)):
                if i in blacklist:
                    continue
                current_button = button_masks[i]
                next_state = [a + b for a, b in zip(previous_state, current_button)]

                if next_state == expected_state:
                    current_record[0] = count + 1
                    return

                if any([next_state[j] > expected_state[j] for j in range(len(next_state))]):
                    next_blacklist.append(i)
                    continue
                else:
                    next_states.append(next_state)

            for next_state in next_states:
                push_buttons(expected_state, button_masks, count + 1, next_state, next_blacklist)

        buttons = line[1]
        button_masks = [[1 if i in button else 0 for i in range(len(joltages))] for button in buttons]
        push_buttons(joltages, button_masks, 0, [0 for _ in range(len(joltages))],[])
        number_of_tries.append(current_record[0])
    return sum(number_of_tries)


def process_input(input):
    output = []
    for line in input:
        initial_split = line.split(' ')
        expected_state = [False if char == '.' else True for char in initial_split[0][1:-1]]
        joltages = [int(i) for i in initial_split[-1][1:-1].split(',')]
        buttons = [[int(i) for i in tuples[1:-1].split(',')] for tuples in initial_split[1:-1]]
        output.append((expected_state, buttons, joltages))
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
