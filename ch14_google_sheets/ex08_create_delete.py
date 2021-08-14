import ezsheets


ss = ezsheets.createSpreadsheet('Multiple Sheets')
print(ss.sheetTitles)               # ('Sheet1',)
ss.createSheet('Spam')              # Create a new sheet at the end of the list of sheets.

ss.createSheet('Eggs')              # Create another new sheet.
print(ss.sheetTitles)               # ('Sheet1', 'Spam', 'Eggs')
ss.createSheet('Bacon', 0)          # Create a sheet at index 0 in the list of sheets.
print(ss.sheetTitles)               # ('Bacon', 'Sheet1', 'Spam', 'Eggs')

ss[0].delete()                      # Delete the sheet at index 0: the "Bacon" sheet.
print(ss.sheetTitles)               # ('Sheet1', 'Spam', 'Eggs')
ss['Spam'].delete()                 # Delete the "Spam" sheet.
print(ss.sheetTitles)               # ('Sheet1', 'Eggs')

sheet = ss['Eggs']                  # Assign a variable to the "Eggs" sheet.
sheet.delete()                      # Delete the "Eggs" sheet.
print(ss.sheetTitles)               # ('Sheet1',)

ss[0].clear()                       # Clear all the cells on the "Sheet1" sheet.
print(ss.sheetTitles)               # The "Sheet1" sheet is empty but still exists. ('Sheet1',)
