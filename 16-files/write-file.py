filename = '../out/programming.txt'

# options on a file are append (a), read (r), write (w), read-write (r+)
# if opening a file in 'w', if the file exists, Python will erase the content
with open(filename, 'w') as file_object :
    file_object.write("I love programming!")

# multiple lines
with open(filename, 'w') as file_object :
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# append to a file
with open(filename, 'a') as file_object :
    file_object.write("I love finding meaning in datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
