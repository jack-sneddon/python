# utility to replace files with '-' with '_'
import os

# todo - add recursion
# todo - add extension filtering
def replace_dashes(dirname) :
    print(f"Replacing files in {dirname} with dashes to be underscores")
    for filename in os.listdir(dirname):
        if(filename.find('-') != -1) :
            print(filename)
            newfilename = filename.replace('-','_')
            print(newfilename)
            os.rename(filename, newfilename)

def replace_dashes_tree(dirname):
    print(dirname)



replace_dashes("../out")
replace_dashes_tree("../out")