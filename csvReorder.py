################
# csvReorder.py - filter a csv file based on another
################

#VARIABLES
FILTERFILE =
RAWFILE =
OUTPUTFILE =


# open the filter file
csvFilterFile = open(FILTERFILE)
filterReader = csv.reader(csvFilterFile)

# open the raw file
csvRawFile = open(RAWFILE)
rawReader = csv.reader(csvRawFile)

# open the output file
csvOutputFile = open(OUTPUTFILE, 'w', newline='')
outputWriter = csv.writer(csvOutputFile)

# dump a smaller section of the larger file
