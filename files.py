#!/usr/bin/python
####################
# chapter 14 of automate the boring stuff
# csv manipulation
####################

import csv
import os

# check the working dir
cwd = os.getcwd()
print ('cwd:', cwd)


######### INPUT #############
# open the file to be used
inputFile = open('output.tsv')
print('inputfile opened')

# pass to the csv reader
reader = csv.reader(inputFile)

# the reader object can only be used once!!!!!

# put the csv read data into a list
#data = list(reader)
#print (data)

# read the file line by line to save memories
for row in reader:
    print("Row", str(reader.line_num), str(row))

# close the input file
inputFile.close()

######## OUTPUT ############ 

# open the output file
outputFile = open('output.tsv', 'w', newline='')
print ('output file opened')

# pass to the output file to the csv writer
outputWriter = csv.writer(outputFile)
#outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')

# some example output
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])

# close the file!
outputFile.close()

print ("Done!")










