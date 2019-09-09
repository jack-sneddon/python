#
# Read an entire file
# 

# 'with' closes access to the file once access is no longer needed 
# so don't call close() - timing of close can be tricky considering bugs or logic errors

with open('../files/pi_digits.txt') as file_object:
    contents = file_object.read()

# store the entire content of the file as a string into 'contents'
# contents has an extra line because the read pulls up a blank line, use rstrip to clean up
print(contents.rstrip())


#
# Read line-by-line
# 
filename = '../files/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# make a list of lines from a file and print out one long string
filename = '../files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
pi_number = float(pi_string)
print(pi_number)

# working with large files
filename = '../files/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))



