import csv
import os

state_capitals_cvs = "../files/state_capitals.csv"

#Setup
if os.path.isfile(state_capitals_cvs) :
    print("read " + state_capitals_cvs)
else :
    print("Error: file missing: " + state_capitals_cvs )


'''
   Count how many rows in a csv file 
'''
capitalsFile = open(state_capitals_cvs)
capitalsDictReader = csv.DictReader(capitalsFile)

row_count = sum(1 for row in capitalsFile)
print("number of rows = " + str(row_count))

capitalsFile.close()