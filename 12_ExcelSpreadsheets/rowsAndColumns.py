import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

tuple(sheet['A1':'C3'])

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)

    print('---End of Row ---')

sheet = wb.active

# apparently the sheet.columns[1] recommended in the book is no longer supported by openpyxl
# instead of columns, have to just select the whole column by column name, eg the letter 
# otherwise get a 'object is not subscriptable
for obj in sheet['A']:
    print(obj.value)