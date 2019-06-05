#! python3
# removeCsvHeader.py - Removes the header from all CSV Files 
# in the current working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv')
    continue

print('removing header from ' + csvFilename + '...')

