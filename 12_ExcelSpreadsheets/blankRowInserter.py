import openpyxl
import sys

rowNumber = sys.argv[1]
blanksToInsert = sys.argv[2]
spreadSheet = sys.argv[3]

wb = openpyxl.load_workbook(spreadSheet)

sheet = wb.active

for row in range(1, rowNumber):

# capture and save data from spreadsheet 

# insert # of rows from blanksToInsert variable

# remaining data from spreadsheet

# the first portion + blanks + second portion to new spreadsheet

# save spreadsheet