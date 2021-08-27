import ezgmail

resultThreads  = ezgmail.search('RoboCop')
print(len(resultThreads))

print(ezgmail.summary(resultThreads))
