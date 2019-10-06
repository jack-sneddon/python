import os
import shutil
import sys

# get the current working directory
directory = os.getcwd()
print(directory)

# without a path, it uses the current working directory
# but we could pass in the path to get the list
list_dir = os.listdir()
print("\nFiles and directories in '", os.getcwd(), "' :") 
print (list_dir)

# create a directory
#
new_dir_1 = "dir1"
new_dir_2 = "dir2"

dir1_path = ""

try :
    # create the path - join handles the file seperators
    print("\n+++++ Create a directory")
    dir1_path = os.path.join(directory, new_dir_1) 
    # create the directory
    os.makedirs(dir1_path, exist_ok = True) 
    print("Directory '%s' created" %new_dir_1) 
except OSError as error: 
    print("Directory '%s' can not be created" %new_dir_1) 

# change directory aka - cd
os.chdir(new_dir_1)

# copy a file or directory — cp
print("\n+++++ Copy a file to a new directory")
src_dir = "src"
src_file = "file1.txt"

copy_src = os.path.join(directory, src_dir, src_file) 

try :
    shutil.copy2(copy_src, ".")
    print("Copied '%s' " %src_file) 
    list_dir = os.listdir()
    print(list_dir)
except OSError as error: 
    print("Cannot copy '%s' " %src_file) 

# move a file
print("\n+++++ move a file to a new directory")
sub_dir = "dir2"

try :
    os.makedirs(sub_dir)
    shutil.move(src_file, sub_dir)
    print("Copied '%s' " %src_file) 
    print(os.listdir(sub_dir))
except OSError as error: 
    print("Cannot move file '%s' " %src_file) 

# Walk the directory
print("\n+++++ Walk dir1")
for dir_path, dir_names, file_names in os.walk(dir1_path):
    for d in dir_names:
        print(d)

    for f in file_names:
        print(f)

# clean up
print("\n+++++ Cleanup")
try :    
    os.chdir(sub_dir) 
    # remove a file — rm
    os.remove(src_file) 
    # remove a tree - rm -rf
    os.chdir(directory)
    shutil.rmtree(dir1_path)
except OSError as error: 
    print("Cannot remove file '%s' " %src_file) 

# validate
os.chdir(directory)
for dir_path, dir_names, file_names in os.walk(dir1_path):
    for d in dir_names:
        assert(d != new_dir_1)
        assert(d != new_dir_2)
    for f in file_names:
        assert(f != src_file)

