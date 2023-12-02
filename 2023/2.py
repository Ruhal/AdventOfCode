input_file = open("input.txt"  , 'r').read().split('\n')
colour_count = {"red":12, "green":13, "blue":14}     

def valid_game(i,line):
    start = line.index(":")+2
    line = line[start:]
    reveals = line.split("; ")
    
    for reveal in reveals:
        for combo in reveal.split(", "):
            count, colour = combo.split(" ")
            if int(count) > colour_count[colour]:
                return 0
        
    return i+1

print(sum(valid_game(i,line) for i,line in enumerate(input_file)))

def find_power(i,line):
    colour_count = {"red":0, "green":0, "blue":0}     
    start = line.index(":")+2
    line = line[start:]
    reveals = line.split("; ")
    
    for reveal in reveals:
        for combo in reveal.split(", "):
            count, colour = combo.split(" ")
            colour_count[colour] = max(int(count), colour_count[colour])
        
    return colour_count["red"]*colour_count["green"]*colour_count["blue"]

print(sum(find_power(i,line) for i,line in enumerate(input_file)))