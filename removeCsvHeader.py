#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the cwd

import csv, os

os.makedirs('headersRemoved'. exist_ok=True)

# Loop through every file in cwd
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip files without csv

    print ("Removing header from", csvFilename, '...')

    # TODO: read the csv file in

    # TODO: write out the new csv file
