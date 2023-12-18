import itertools

input_file = open(r"input.txt", 'r').read()
grid= [list(x) for x in input_file.split('\n')]
row_expand, column_expand, position = [],[],[]
total=0
expand_count=1000000 # change to 2 for part 1

for i in range(len(grid)):
    if len(set(grid[i]))==1:  
        row_expand.append(i)
    for j in range(len(grid[0])):
        if grid[i][j]=='#':
            position.append([i, j])

for j in range(len(grid[0])):    
    if len(set([grid[i][j] for i in range(len(grid))]))==1:
            column_expand.append(j)

for combination in list(itertools.combinations(position, 2)):
    p1 = combination[0]
    p2 = combination[1]
    distance = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    row_count = len(set(range(min(p1[0],p2[0]),max(p1[0],p2[0]))) & set(row_expand))
    col_count = len(set(range(min(p1[1],p2[1]),max(p1[1],p2[1]))) & set(column_expand))
    distance += expand_count * (row_count+col_count) - row_count - col_count
    total+=distance
    
print(total)