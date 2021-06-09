import pyinputplus as pyip
# See https://pyinputplus.readthedocs.io/


response = pyip.inputNum()
print(response)

response = pyip.inputInt(prompt='Enter a number: ')
print(response)

# min, max, greaterThan and lessThan arguments
response = pyip.inputNum('Enter num: ', min=4)
print(response)

response = pyip.inputNum('Enter num: ', greaterThan=4)
print(response)

# blank argument
# By default, blank input isn't allowed
response = pyip.inputNum(blank=True)

# limit, timeout and default arguments
# Number of attempts before valid answer
response = pyip.inputNum(limit=2)

# Timeout before valid answer
response = pyip.inputNum(timeout=20)

response = pyip.inputNum(limit=2, default='N/A')

# allowRegexes and blockRegexes arguments
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])

response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# allow list overrides the block list
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])

# custom validation
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception(f'The digits must add up to 10, not {sum(numbersList)}.')

response = pyip.inputCustom(addsUpToTen)
