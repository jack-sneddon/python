import os
import csv

# setup
# setup
output_file = "output.csv"
if os.path.isfile(output_file) :
    os.remove(output_file)

outputFile = open(output_file, 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': "cat", 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Pet': "aligator", 'Phone': '666-5432'})
outputDictWriter.writerow({'Name': 'Jane', 'Pet': "dog", 'Phone': '777-6776'})

outputFile.close()