ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)                 # [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
print(ages)                 # [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.