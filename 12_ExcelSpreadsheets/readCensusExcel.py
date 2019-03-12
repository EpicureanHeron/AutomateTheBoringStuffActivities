import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')

sheet = wb.get_sheet_by_name('Population by Census Tract')

countyData = {}

