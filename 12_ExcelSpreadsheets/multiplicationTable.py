import openpyxl
import sys

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, int(sys.argv[1]) + 1): 
    sheet['A' + str(i+1)] = i
    sheet[openpyxl.utils.get_column_letter(i+1) + '1'] = i

wb.save('multiTables.xlsx')