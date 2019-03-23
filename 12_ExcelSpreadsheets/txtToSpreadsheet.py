import openpyxl
import sys

f1 = open(sys.argv[1], 'r+')
f2 = open(sys.argv[2], 'r+')

wb = openpyxl.Workbook()
sheet = wb.active


counter = 1
for line in f1:
    line = line.strip('\n')
    sheet['A' + str(counter)].value = line
    counter += 1
   
counter = 1
for line in f2:
    line = line.strip('\n')
    sheet['B' + str(counter)].value = line
    counter += 1


wb.save('outputTxtToSpreadsheet.xlsx')