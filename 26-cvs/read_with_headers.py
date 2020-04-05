import csv
import os

example_with_headers_file = "../files/exampleWithHeader.csv"
example_without_headers_file = "../files/example.csv"

#Setup
if os.path.isfile(example_with_headers_file) :
    print("read " + example_with_headers_file)
else :
    print("Error: file missing: " + example_with_headers_file )

if os.path.isfile(example_without_headers_file) :
    print("read " + example_without_headers_file)
else :
    print("Error: file missing: " + example_without_headers_file )

'''
    the DictReader object sets row to a dictionary object with 
    keys derived from the headers in the first row

    So by default, it skips the first row
'''
exampleFile = open(example_with_headers_file)
exampleDictReader = csv.DictReader(exampleFile)

for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

print ('\n --- \n')
'''
    if I don't have headers and want to use the DictReader, 
    set them manually with a second argument containing 
    the made up header names
'''
exampleFile = open(example_without_headers_file)
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])

for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])

exampleFile.close()