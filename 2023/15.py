input_file = open(r"input.txt", 'r').read()
boxes = [[] for i in range(256)]

def get_hash(string):
    curr=0
    for char in list(string):
        curr = ((curr+ord(char))*17) % 256
        
    return curr

for step in input_file.split(','):
    label = step.split("=")[0] if "=" in step else step.split("-")[0]
    num=get_hash(label)
    box = boxes[num]
    matches = [x for x in box if label == x.split("=")[0]]
    
    if "=" in step:
        if len(matches)>0:
            box[box.index(matches[0])]=step
        else:
            box.append(step)     
    elif len(matches)>0:
        box.pop(box.index(matches[0]))
        
    boxes[num]=box
        
total=0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        total+= (i+1)*(j+1) * float(boxes[i][j].split("=")[1])

print(sum(get_hash(step) for step in input_file.split(',')))
print(total)