#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the cwd

import csv, os

os.makedirs('headersRemoved', exist_ok=True)

# Loop through every file in cwd
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip files without csv

    print ("Removing header from", csvFilename, '...')

    # read the csv file in
    csvRows = []
    csvFile = open(csvFilename)
    reader = csv.reader(csvFile)
    for row in reader:
        if reader.line_num==1:
            continue # skip the first row
        csvRows.append(row)
    csvFile.close()

    # write out the new csv file
    print ("Writing to", os.path.join('headersRemoved', csvFilename))
    csvFile = open(os.path.join('headersRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFile)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFile.close()
