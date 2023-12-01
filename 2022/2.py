input_file = open("input.txt"  , 'r').read().split('\n')
opp = {'A':0, 'B':1, 'C':2}
me = {'X':0, 'Y':1, 'Z':2}

def round_points(line):
    opp_move = opp[line[0]]
    me_move = me[line[-1]]
    if opp_move == me_move:
        return 3 + me_move + 1
    elif opp_move == int(((me_move + 1) % 3)):
        return 0 + me_move + 1
    else:
        return 6 + me_move + 1

points = [round_points(line) for line in input_file]
print(sum(points))

def round_points_2(line):
    opp_move = opp[line[0]]
    round_status = line[-1]
    if round_status == 'Y':
        return 3 + opp_move + 1
    elif round_status == 'X':
        return 0 + ((opp_move - 1) % 3) + 1
    elif round_status == 'Z':
        return 6 + ((opp_move + 1) % 3) + 1
    
points = [round_points_2(line) for line in input_file]
print(sum(points))