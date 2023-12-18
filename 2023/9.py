import re

input_file = open(r"input.txt", 'r').read().split('\n')
seqs = [[] for i in range(len(input_file))]

for index in range(len(input_file)):
    numbers =[int(i) for i in re.findall(r'([-]\d+|\d+)', input_file[index])]
    seqs[index].append(numbers)
    while not len(set(numbers))==1:    
        numbers = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
        seqs[index].append(numbers)       
    
next_vals=[sum(i[-1] for i in k) for k in seqs]
print(sum(next_vals))
previous_vals=[sum(i[0]*(1 if c%2==0 else -1) for c,i in enumerate(k))  for k in seqs]
print(sum(previous_vals))    