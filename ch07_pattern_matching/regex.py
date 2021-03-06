import re


# Matching regex objects
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print(f'Phone number found: {mo.group()}')

# Grouping with parentheses
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print(mo.group(1))      # 415
print(mo.group(2))      # 555-4242
print(mo.group(0))      # 415-555-4242
print(mo.group())       # 415-555-4242
print(mo.groups())      # ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)         # 415
print(mainNumber)       # 555-4242

# Escape characters
phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is (415) 555-4242.')
print(mo.group(1))      # (415)
print(mo.group(2))      # 555-4242

# Matching multiple groups with pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())      # Batman
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())      # Tina Fey

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())       # Batmobile
print(mo.group(1))      # mobile

# Optional matching with the question mark
batRegex = re.compile(r'Bat(wo)?man')           # 0 or 1
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())      # Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())      # Batwoman

# Matching zero or more with the star
batRegex = re.compile(r'Bat(wo)*man')           # 0 or more
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())      # Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())      # Batwoman
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())      # Batwowowowoman

# Matching one or more with the plus
batRegex = re.compile(r'Bat(wo)+man')           # 1 or more
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())      # Batwoman
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())      # Batwowowowoman
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)      # True

# Matching Specific Repetitions with Braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())      # HaHaHa
mo2 = haRegex.search('Ha')
print(mo2 == None)      # True

# Greedy and non-greedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())      # HaHaHaHaHa
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())      # HaHaHa

# The findall() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())       # 415-555-9999

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')                   # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))   # ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')             # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))   # [('415', '555', '9999'), ('212', '555', '0000')]

# Character Classes
'''
\d              Any numeric digit from 0 to 9.
\D              Any character that is not a numeric digit from 0 to 9.
\w              Any letter, numeric digit, or the underscore character. (Think of this as matching ???word??? characters.)
\W              Any character that is not a letter, numeric digit, or the underscore character.
\s              Any space, tab, or newline character. (Think of this as matching ???space??? characters.)
\S              Any character that is not a space, tab, or newline.
'''
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# Making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))     # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
consonantRegex = re.compile(r'[^aeiouAEIOU]')                       # negative class
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')) # ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

# The caret and dollar sign characters
beginsWithHello = re.compile(r'^Hello')                     # Start of string
print(beginsWithHello.search('Hello, world!'))              # <re.Match object; span=(0, 5), match='Hello'>
print(beginsWithHello.search('He said hello.') == None)     # True

endsWithNumber = re.compile(r'\d$')                                 # End of string
print(endsWithNumber.search('Your number is 42'))                   # <re.Match object; span=(16, 17), match='2'>
print(endsWithNumber.search('Your number is forty two.') == None)   # True

wholeStringIsNum = re.compile(r'^\d+$')                     # Start and end
print(wholeStringIsNum.search('1234567890'))                # <re.Match object; span=(0, 10), match='1234567890'>
print(wholeStringIsNum.search('12345xyz67890') == None)     # True
print(wholeStringIsNum.search('12  34567890') == None)      # True

# The wildcard character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))       # ['cat', 'hat', 'sat', 'lat', 'mat']

# Matching everything with dot-star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))                                          # Al
print(mo.group(2))                                          # Sweigart

nongreedyRegex = re.compile(r'<.*?>')                       # Non-greedy
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())                                           # <To serve man>
greedyRegex = re.compile(r'<.*>')                           # Non-greedy
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())                                           # <To serve man> for dinner.>

# Matching newlines with the dot character
noNewlineRegex = re.compile('.*')
x = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.nUphold the law.').group()
print(x)                                                    # Serve the public trust.

newlineRegex = re.compile('.*', re.DOTALL)
x = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(x)                                                    # Serve the public trust.\nProtect the innocent.\nUphold the law.

# Review of Regex Symbols
'''
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn???t between the brackets.
'''

# Case-insensitive matching
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machhine, all cop.').group())                       # RoboCop
print(robocop.search('ROBOCOP protects the innocent.').group())                                     # ROBOCOP
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())     # robocop

# Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))        # CENSORED gave the secret documents to CENSORED.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
# A**** told C**** that E**** knew B**** was a double agent.

# Managing Complex Regexes
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
