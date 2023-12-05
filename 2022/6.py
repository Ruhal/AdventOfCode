def get_start(string,distinct_count):
    for i in range(len(string)):
        if len(set([k for k in string[i:i+distinct_count]]))==distinct_count:
            return i+distinct_count

input_file = open(r"input.txt"  , 'r').read()
print(get_start(input_file,4))
print(get_start(input_file,14))