import itertools
import os
from common.file_utils import example_as_lines, input_as_lines


def from_to(input, start, end):
    devices = [start]
    already_visited = [start]
    count = 0
    while len(devices) > 0:
        new_devices = []
        for device in devices:
            next_devices = input[device]
            for next_device in next_devices:
                if next_device == end:
                    count += 1
                    continue
                if next_device in already_visited:
                    continue
                already_visited.append(next_devices)
                new_devices.append(next_device)
        devices = new_devices
    return count

def part_1(input):
    return from_to(input, 'you', 'out')


def part_2(input):
    devices = {
        'nothing': ['svr'],
        'fft': [],
        'dac': [],
        'both': []
    }
    already_visited = ['svr']

    count = 0
    while len(list(itertools.chain.from_iterable(devices.values()))) > 0:
        new_devices = {
            'nothing': [],
            'fft': [],
            'dac': [],
            'both': []
        }
        for key in devices.keys():
            for device in devices[key]:
                next_devices = input[device]
                for next_device in next_devices:
                    if next_device == 'out':
                        if key == 'both':
                            count += 1
                        continue
                    if next_device in already_visited:
                        continue
                    already_visited.append(next_devices)
                    if key == 'nothing':
                        if next_device == 'fft':
                            new_devices['fft'].append(next_device)
                        elif next_device == 'dac':
                            new_devices['dac'].append(next_device)
                        else:
                            new_devices['nothing'].append(next_device)
                    elif key == 'fft':
                        if next_device == 'dac':
                            new_devices['both'].append(next_device)
                        else:
                            new_devices['fft'].append(next_device)
                    elif key == 'dac':
                        if next_device == 'fft':
                            new_devices['both'].append(next_device)
                        else:
                            new_devices['dac'].append(next_device)
                    elif key == 'both':
                        new_devices['both'].append(next_device)
        devices = new_devices
    return count


def process_input(input):
    out = {}
    for line in input:
        split_parts = line.strip().split(' ')
        out[split_parts[0][0:-1]] = split_parts[1:]
    return out


if __name__ == '__main__':
    parent_folder = os.path.basename(os.path.dirname(__file__))
    example = example_as_lines(parent_folder)
    example_2 = 'svr: aaa bbb,aaa: fft,fft: ccc,bbb: tty,tty: ccc,ccc: ddd eee,ddd: hub,hub: fff,eee: dac,dac: fff,fff: ggg hhh,ggg: out,hhh: out'.split(',')
    input = input_as_lines(parent_folder)

    print("example part_1")
    print(part_1(process_input(example)))
    print("input part_1")
    print(part_1(process_input(input)))

    print("example part_2")
    print(part_2(process_input(example_2)))
    print("input part_2")
    print(part_2(process_input(input)))
