import csv
import os

'''
    using reader and writer read and writes rows using lists
    DictReader and DictWriter do the same thing, but use dictionaries
        and the first row is the key
'''

# setup
bond_villian_file = "~/villians.csv"
if os.path.isfile(bond_villian_file) :
    os.remove(bond_villian_file)

# write a CSV file - for reading
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'}
]

with open('villians.csv', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

# read a CSV file -- good for smaller data sets
with open('villians.csv', newline='') as cvsfile:
    # convert it to a Python list which I can store in a variable
    bond_villians = list(csv.reader(cvsfile))  

print("print list")
print(bond_villians)
print("second row = " + bond_villians[1][0] + " " + bond_villians[1][1])

print("\n----\n")
'''
  reader iterates over the rows - when there are huge datasets

  reader object can be looped over only once.  To reread the CSV file, 
  you must call csv.reader to create a new reader object
'''
print("print rows")
with open('villians.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print('Row #' + str(csvReader.line_num) + ' ' + str(row))
