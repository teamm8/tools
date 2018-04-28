################
# csvReorder.py - filter a csv file based on another
################

#VARIABLES
FILTERFILE =
RAWFILE =
OUTPUTFILE =

# open the raw file
csvRawFile = open(RAWFILE)
rawReader = csv.reader(csvRawFile)

# open the filter file
csvFilterFile = open(FILTERFILE)
filterReader = csv.reader(csvFilterFile)

# open the output file
csvOutputFile = open(OUTPUTFILE, 'w', newline='')
outputWriter = csv.writer(csvOutputFile)

def getraw(filename, criterion):
    with open(filename) as csvfile:
        datareader = csv.reader(csvfile)
        count = 0
        for row in datareader:
            if row[3] in ("column header", criterion):
                yield row
                count += 1
            elif count < 2:
                continue
            else:
                return

def getdata(filename, criteria):
    for criterion in criteria:
        for row in getraw(filename, criterion):
            yield row

for row in getdata(somefilename, sequence_of_criteria):
    # process row



# dump a smaller section of the larger file
for rawRow in rawReader:
    if rawReader.line_num == 1:
        outputWriter.writeline(



