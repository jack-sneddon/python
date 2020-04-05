import os
import csv

'''
    using reader and writer read and writes rows using lists
    DictReader and DictWriter do the same thing, but use dictionaries
        and the first row is the key
'''

# setup
output_file = "output.csv"
if os.path.isfile(output_file) :
    os.remove(output_file)

# write a CSV file - for reading
outputFile = open(output_file, 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# how will the csv library handle the comma in the hello world statement?
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['tomatoes', 'eggs', 'bacon', 'spam'])
outputWriter.writerow([1, 2, 3.141569, 4])

outputFile.close()

'''
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
'''