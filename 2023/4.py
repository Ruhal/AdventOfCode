import re

def win_count(line):      
    winners=re.findall(r'(\d+)',line[line.index(":")+2:line.index("|")+1])
    card=re.findall(r'(\d+)',line[line.index("|")+1:])
    return sum(1 for i in card if i in winners)

input_file = open(r"input.txt"  , 'r').read().split('\n')
win_counts = [win_count(line) for line in input_file]
print(sum(pow(2, count-1) if count>0 else 0 for count in win_counts))

def f(i,line): 
    global value  
    value += 1    
    for x, line2 in enumerate(input_file[i+1:(i+1+win_count(line))]):
        f(i+1+x,line2)

value = 0.0
for i, line in enumerate(input_file):
    f(i, line)
 
print(value)     