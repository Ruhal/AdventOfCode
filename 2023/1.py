import re

data = open("input.txt", 'r').read().split('\n')

def get_number_1(string):
  m1 = re.search(r"\d", string)
  m2= re.search(r"\d", string[::-1])
  return int(string[m1.start()] + string[len(string) - m2.start()-1])

print(sum(get_number_1(x) for x in data))

one_to_nine = {'one':"1", 'two':"2", 'three':"3", 'four':"4", 'five':"5", 'six':"6", 'seven':"7", 'eight':"8", 'nine':"9"}

def get_number_2(string):
  m = re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))',string)
  m = [match.group(1) for match in m]
  first_digit=m[0]
  second_digit=m[-1]
  if first_digit in one_to_nine.keys():
      first_digit = one_to_nine[first_digit]      
  if second_digit in one_to_nine.keys():
      second_digit = one_to_nine[second_digit]    
  return int(first_digit + second_digit)

print(sum(get_number_2(x) for x in data))