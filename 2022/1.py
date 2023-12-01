elf_calories = ([sum(x) for x in [map(int,x.split('\n')) for x in open("input.txt"  , 'r').read().split('\n\n')]])
print(max(elf_calories))
elf_calories.sort()
print(sum(elf_calories[-3:]))