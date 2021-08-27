import ezgmail


unreadThreads = ezgmail.unread() # List of GmailThread objects.
print(ezgmail.summary(unreadThreads))


print(len(unreadThreads))
print(str(unreadThreads[0]))
print(len(unreadThreads[0].messages))
print(str(unreadThreads[0].messages[0]))
print(unreadThreads[0].messages[0].subject)
print(unreadThreads[0].messages[0].body)
print(unreadThreads[0].messages[0].timestamp)
print(unreadThreads[0].messages[0].sender)
print(unreadThreads[0].messages[0].recipient)

recentThreads = ezgmail.recent()                    # default: 25
print(len(recentThreads))
recentThreads = ezgmail.recent(maxResults=100)
print(len(recentThreads))
