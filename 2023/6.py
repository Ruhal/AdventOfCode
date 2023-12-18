import math, re
   
def get_range(t,r):
    x1=(t+math.sqrt(t**2-4*r))/2
    x2=(t-math.sqrt(t**2-4*r))/2
    x1 = x1-1 if x1.is_integer() else math.floor(x1)
    x2 = x2+1 if x2.is_integer() else math.ceil(x2)
    return x1-x2+1

input_file = open(r"input.txt", 'r').read().split('\n')
time = [float(x) for x in re.findall(r'(\d+)',input_file[0])]
record = [float(x) for x in re.findall(r'(\d+)',input_file[1])]
ranges = [get_range(time[i],record[i]) for i in range(len(time))]
print(math.prod(ranges))
time = float("".join([x for x in re.findall(r'(\d+)',input_file[0])]))
record = float("".join([x for x in re.findall(r'(\d+)',input_file[1])]))
print(get_range(time,record))