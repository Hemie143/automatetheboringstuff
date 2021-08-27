import ezgmail


threads = ezgmail.search('pictures')
print(threads[0].messages[0].attachments)
print(threads[0].messages[0].downloadAttachment('tulips.jpg'))
threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2019')