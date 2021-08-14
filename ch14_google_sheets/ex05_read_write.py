import ezsheets


ss = ezsheets.createSpreadsheet('My Spreadsheet')
sheet = ss[0]               # Get the first sheet in this spreadsheet.
print(sheet.title)
sheet = ss[0]
sheet['A1'] = 'Name'        # Set the value in cell A1.
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'
print(sheet['A1'])          # Read the value in cell A1.
print(sheet['A2'])          # Empty cells return a blank string.
print(sheet[2, 1])          # Column 2, Row 1 is the same address as B1.
sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'RoboCop'

sheet.refresh()
