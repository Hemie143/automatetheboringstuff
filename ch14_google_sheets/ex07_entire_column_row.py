import ezsheets


ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]
print(sheet.getRow(1))          # The first row is row 1, not row 0. ['PRODUCE', 'COST PER POUND', 'POUNDS SOLD', 'TOTAL', '', '']
print(sheet.getRow(2))          # ['Potatoes', '0.86', '21.6', '18.58', '', '']

columnOne = sheet.getColumn(1)
print(sheet.getColumn(1))       # ['PRODUCE', 'Potatoes', 'Okra', 'Fava beans', 'Watermelon', 'Garlic',
print(sheet.getColumn('A'))     # Same result as getColumn(1)

print(sheet.getRow(3))          # ['Okra', '2.26', '38.6', '87.24', '', '']
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
print(sheet.getRow(3))          # ['Pumpkin', '11.50', '20', '230', '', '']

columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    # Make the Python list contain uppercase strings:
    columnOne[i] = value.upper()

sheet.updateColumn(1, columnOne)    # Update the entire column in one request.

rows = sheet.getRows()              # Get every row in the spreadsheet.
print(rows[0])                      # Examine the values in the first row.

print(rows[1])                      # ['POTATOES', '0.86', '21.6', '18.58', '', '']
rows[1][0] = 'PUMPKIN'              # Change the produce name.
print(rows[1])                      # ['PUMPKIN', '0.86', '21.6', '18.58', '', '']

print(rows[10])                     # ['OKRA', '2.26', '40', '90.4', '', '']
rows[10][2] = '400'                 # Change the pounds sold.
rows[10][3] = '904'                 # Change the total.
print(rows[10])                     # ['OKRA', '2.26', '400', '904', '', '']

sheet.updateRows(rows)              # Update the online spreadsheet with the changes.

print(sheet.rowCount)               # The number of rows in the sheet. 23758
print(sheet.columnCount)            # The number of columns in the sheet. 6
sheet.columnCount = 4               # Change the number of columns to 4.
print(sheet.columnCount)            # Now the number of columns in the sheet is 4. 4
