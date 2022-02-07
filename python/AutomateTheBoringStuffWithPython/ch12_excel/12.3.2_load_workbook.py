import openpyxl
wb = openpyxl.openpyxl.Workbook('.\python\\AutomateTheBoringStuffWithPython\\ch12\\example.xlsx')
sheet = wb.get_sheet_name()
print(sheet['A1'])
print(sheet['A1'].value)
c = sheet['B1']
print('Row ' + str(c.row) + ', Column ' + str(c.column) + ' is ', '')
print(c.value)
print('Cell ' + c.coordinate + ' is ' + str(c.value))