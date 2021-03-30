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
batRegex = re.compile(r'Bat(wo)*man')           # 0 or 1
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())      # Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())      # Batwoman
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())      # Batwowowowoman