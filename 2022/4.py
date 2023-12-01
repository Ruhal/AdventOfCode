import re

input_file = open("input.txt"  , 'r').read().split('\n')

def full_overlap(line):
    sections = re.split(",|-",line)
    
    if (int(sections[0])>=int(sections[2])) & (int(sections[1])<=int(sections[3])):
        return 1
    elif (int(sections[2])>=int(sections[0])) & (int(sections[3])<=int(sections[1])):
        return 1
    else:
        return 0

print(sum(full_overlap(line) for line in input_file))

def any_overlap(line):
    sections = re.split(",|-",line)

    if (int(sections[1]) < int(sections[2])) | (int(sections[0]) > int(sections[3])):
        return 0
    else:
        return 1    

print(sum(any_overlap(line) for line in input_file))