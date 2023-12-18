import re
from collections import Counter

input_file = open(r"input.txt", 'r').read().split('\n')
cards = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))
types = {i:[] for i in range(1,8)}
  
def type(line, joker_exists):
    hand = line.split(' ')[0]
    a = Counter(re.findall(r'(A|K|Q|J|T|9|8|7|6|5|4|3|2)', hand))
    count = list(a.values())
    
    if joker_exists and 'J' in a.keys() and len(count)>1:
        j_count = a['J']
        count.remove(j_count)
        count.sort()
        count[-1]+=j_count
        
    if len(count)==1:
        return 7
    elif len(count)==2:
        if 4 in count:
            return 6
        elif 3 in count and 2 in count:
            return 5
    elif len(count)==3:
        if 3 in count:
            return 4
        else:
            return 3
    elif len(count)==4:
        return 2
    else:
        return 1
                

for line in input_file:
    types[type(line,False)].append(line)
        
for i in types.keys():
    temp = types[i]
    temp.sort(key=lambda x: (cards.index(x[0]),cards.index(x[1]),cards.index(x[2]),cards.index(x[3]),cards.index(x[4])))
    types[i]=temp
   
rank=0
sum1=0
for item in types.values():
    for line in item:
        rank+=1
        sum1+=rank*float(line.split(' ')[1])
        
print(sum1)   

cards = list(reversed(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J',]))
types = {i:[] for i in range(1,8)}
for line in input_file:
    types[type(line,True)].append(line)
        
for i in types.keys():
    temp = types[i]
    temp.sort(key=lambda x: (cards.index(x[0]),cards.index(x[1]),cards.index(x[2]),cards.index(x[3]),cards.index(x[4])))
    types[i]=temp
   
rank=0
sum1=0
for item in types.values():
    for line in item:
        rank+=1
        sum1+=rank*float(line.split(' ')[1])
        
print(sum1)   