input_file = open(r"input.txt", 'r').read()
grid= input_file.split('\n')

for i in range(len(grid)):
    if 'S' in grid[i]:
        start = [i, grid[i].index('S')]

def get_moves(pipe):
    if pipe=='-':
        return [[0,-1],[0,1]]
    if pipe=='7':
        return [[0,-1],[1,0]]
    if pipe=='|':
        return [[-1,0],[1,0]]
    if pipe=='J':
        return [[-1,0],[0,-1]]
    if pipe=='L':
        return [[-1,0],[0,1]]
    if pipe=='F':
        return [[0,1],[1,0]]
    
def next_pos(prev_pos,pos):
    pipe = grid[pos[0]][pos[1]]
    moves = get_moves(pipe)
    next_moves = [[sum(x) for x in zip(pos, move)] for move in moves]

    for p in next_moves:
        if not p==prev_pos:
            return [pos, p]

prev_pos=start
pos = [94,99]
pipe = grid[pos[0]][pos[1]]
count =1

while not pipe == 'S':
    prev_pos, pos = next_pos(prev_pos, pos)
    pipe = grid[pos[0]][pos[1]]
    count +=1
    
print(count/2)