import re

stack, moves = open(r"C:\Users\Ruhal.Miah\OneDrive - Ariel Re BDA Limited\Spyder\5\input.txt"  , 'r').read().split('\n\n')
crates = stack.split('\n')
cols=crates.pop()
stack_1, stack_2 = {}, {}

for match in re.finditer(r'(\d+)',cols):
    stack_1[match.group()] = [line[match.start()] for line in reversed(crates) if not line[match.start()]==" "]
    stack_2[match.group()] = [line[match.start()] for line in reversed(crates) if not line[match.start()]==" "]

for line in moves.split('\n'):
    count, col_from, col_to = re.findall(r'(\d+)',line)
    for i in range(int(count)):
        stack_1[col_to].append(stack_1[col_from].pop())
        stack_2[col_to].append(stack_2[col_from].pop(len(stack_2[col_from])-int(count)+i))
   
print("".join([v[-1] for v in stack_1.values() if len(v)>0]))
print("".join([v[-1] for v in stack_2.values() if len(v)>0]))