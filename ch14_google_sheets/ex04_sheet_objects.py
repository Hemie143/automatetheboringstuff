import ezsheets


ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
print(ss.sheets)            # The Sheet objects in this Spreadsheet, in order.
print(ss.sheets[0])         # Gets the first Sheet object in this Spreadsheet.
print(ss[0])                # Also gets the first Sheet object in this Spreadsheet.

print(ss.sheetTitles)       # The titles of all the Sheet objects in this Spreadsheet.
print(ss['Classes'])        # Sheets can also be accessed by title.
