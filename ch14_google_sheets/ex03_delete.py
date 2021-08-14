import ezsheets


ss = ezsheets.createSpreadsheet('Delete me')    # Create the spreadsheet.
print(ezsheets.listSpreadsheets())              # Confirm that we've created a spreadsheet.
ss.delete()                                     # Delete the spreadsheet.
print(ezsheets.listSpreadsheets())
