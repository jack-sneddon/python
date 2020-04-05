import os
import csv

'''
    using reader and writer read and writes rows using lists
    DictReader and DictWriter do the same thing, but use dictionaries
        and the first row is the key
'''

# setup
output_file = "output.tsv"
if os.path.isfile(output_file) :
    os.remove(output_file)

# write a CSV file - for reading
csvFile = open(output_file, 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam'])
csvFile.close()

