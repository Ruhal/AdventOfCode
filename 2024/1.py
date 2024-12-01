import os
from pathlib import Path

current_directory = Path().resolve()
os.chdir(current_directory)

import re
numbers = [int(x) for x in re.findall(r'(\d+)',open(r"input.txt", 'r').read())]
col1 = [numbers[2*i] for i in range(len(numbers)//2)]
col2 = [numbers[2*i+1] for i in range(len(numbers)//2)]
col1.sort()
col2.sort()
print(sum(abs(col2[i]-col1[i]) for i in range(len(col1))))

similarity_score=0
for i in range(len(col1)):
    similarity_score+=col1[i] * col2.count(col1[i])
    
print(similarity_score)