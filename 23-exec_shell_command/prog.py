import os

my_command = 'ls -al'
cat_command = 'cat'
out_file = 'out.txt'

directory = os.getcwd()

print(f"\n=== Execute '{my_command}' for {directory}: ")
os.system(my_command)

# store output to a file
my_command = "echo 'hello jack' > " + out_file
print(f"\n=== Execute '{my_command}' for {directory}: ")
os.system(my_command)
my_command = 'cat ' + out_file
print(f"\n=== Execute '{my_command}' for {directory}: ")
os.system(my_command)

# store output to a variable
my_command = os.popen('ls -al').read()
print(f"\n=== Execute to a variable: \n{my_command} ")

#c cleanup
os.remove(out_file) 
