input_file = open("input.txt"  , 'r').read().split('\n')

def get_rucksack_priority(line):
    first = line[:int(len(line)/2)]
    second = line[int(len(line)/2):]
    common_char = list(set(first).intersection(second))[0]
    return get_char_priority(common_char)

def get_char_priority(common_char):
    if common_char.isupper():
        return ord(common_char)-64 + 26
    else:
        return ord(common_char)-96
    
priorities = [get_rucksack_priority(line) for line in input_file]
print(sum(priorities))

def get_badge_priority(data):
    sum_prior = 0
    for i in range(0,len(data)-1,3):        
        first = data[i]
        second = data[i+1]
        third = data[i+2]
        common_char = list(set(first).intersection(second).intersection(third))[0]
        sum_prior += get_char_priority(common_char)
    return sum_prior

print(get_badge_priority(input_file))