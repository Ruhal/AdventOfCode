import re, os

input_file = open(os.path.abspath(os.path.dirname( __file__ )) + r"\input.txt", 'r').read().split(':')
input_file.pop(0)
seeds = [float(x) for x in re.findall(r'(\d+)', input_file.pop(0))]
maps, new_map =[],[]
 
for v in input_file:
    numbers = [float(x) for x in re.findall(r'(\d+)',v)]    
    maps.append([numbers[(3*i):(3*i+3)] for i in range(int(len(numbers)/3))])

def pos_ran(seed,ran):
    for map1 in maps:
        for map2 in map1:
            if map2[1] <= seed < (map2[1] + map2[2]):
                seed = map2[0] + (seed-map2[1]) 
                ran = min(ran,(map2[0] + map2[2]-seed))                                  
                break
    return [seed, ran]

for i in range(int(len(seeds)/2)):
    seed = seeds[2*i] 
    seed_ran = seeds[2*i+1]
    while seed_ran > 0:
        pos1, ran = pos_ran(seed,seed_ran)
        new_map.append([pos1, seed, ran])
        seed+=ran
        seed_ran -=ran
        
print(min([pos_ran(seed,0)[0] for seed in seeds]))       
print(min([map1[0] for map1 in new_map]))