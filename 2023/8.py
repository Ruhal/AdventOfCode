import math, re

def get_steps(node):
    step=0
    while not node[-1]=='Z':
        m=moves[step % len(moves)]    
        step +=1    
        node=nodes[node][0 if m=='L' else 1]
    return step
   
def lcm(a,b):
    return int(a*b/ math.gcd(steps[0], steps[1]))

input_file = open(r"input.txt", 'r').read().split('\n\n') 
moves = input_file[0]
nodes = [re.findall(r'(\w+)', node) for node in input_file[1].split('\n')]
nodes = {x[0]:[x[1],x[2]] for x in nodes} 
steps = [get_steps(x) for x in nodes.keys() if x[-1]=='A']
h = lcm(steps[0], steps[1])
for i in range(2,len(steps)):
    h= lcm(h,steps[i])
    
print(get_steps('AAA'))    
print(h)