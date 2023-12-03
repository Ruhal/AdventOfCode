import math, re

input_file = open("input.txt"  , 'r').read().split('\n')

def has_adjacent(row, start, end):
    for line in input_file[max(0,row-1):row+2]:
        for char in line[max(0,start-1):end+1]:
            if not (char.isdigit() or char=="."):
                    return True
    return False

print(sum(sum(int(line[match.start():match.end()]) for match in re.finditer(r'(\d+)', line) if has_adjacent(i, match.start(), match.end())) for i,line in enumerate(input_file)))

def gear_ratio(row, pos):
    num_list = []
    for line in input_file[max(0,row-1):row+2]:
        for match in re.finditer(r'(\d+)', line):
            if match.start() -1 <= pos <= match.end():
                num_list.append(int(line[match.start():match.end()]))
    return math.prod(num_list) if len(num_list) == 2 else 0

print(sum(sum(gear_ratio(i,match.start()) for match in re.finditer(r'(\*)', line)) for i,line in enumerate(input_file)))