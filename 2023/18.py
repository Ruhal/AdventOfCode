input_file = open(r"input.txt", 'r').read().split('\n')
moves = {'U':[1,0],'D':[-1,0],'L':[0,-1],'R':[0,1]}
moves_2 = {'3':[1,0],'1':[-1,0],'2':[0,-1],'0':[0,1]}
pos, pos_2=[0,0], [0,0]
vertices, vertices_2=[pos], [pos_2]

for line in input_file:
    line = line.split(' ')
    move=[int(line[1]) * x for x in moves[line[0]]]
    pos = [pos[0]+move[0],pos[1]+move[1]]
    vertices.append(pos)
    #part 2
    code = line[2][2:-1]
    size = int(code[:len(code)-1],16) 
    move=[size* x for x in moves_2[code[-1]]]
    pos_2 = [pos_2[0]+move[0],pos_2[1]+move[1]]
    vertices_2.append(pos_2)
           
#shoelace formula
def get_area(vertices):
    perimeter, area= 0.0, 0.0
    
    for i in range(len(vertices)):
        prev= vertices[(i-1) % len(vertices)]
        curr=vertices[i]
        area += (prev[0] + curr[0]) * (prev[1] - curr[1])
        perimeter += abs(prev[0] - curr[0]) + abs(prev[1] - curr[1])
        
    return int(abs(area / 2.0)+ perimeter/2 +1) 

print(get_area(vertices))
print(get_area(vertices_2))