import ezsheets


print(ezsheets.convertAddress('A2'))        # Converts addresses... (1, 2)
print(ezsheets.convertAddress(1, 2))        # ...and converts them back, too.'A2'
print(ezsheets.getColumnLetterOf(2))        # 'B'
print(ezsheets.getColumnNumberOf('B'))      # 2
print(ezsheets.getColumnLetterOf(999))      # 'ALK'
print(ezsheets.getColumnNumberOf('ZZZ'))    # 18278
