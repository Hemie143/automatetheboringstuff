import ezgmail

ezgmail.init()
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')
# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email', ['attachment1.jpg', 'attachment2.mp3'])
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email', cc='friend@example.com',
             bcc='otherfriend@example.com,someoneelse@example.com')

print(ezgmail.EMAIL_ADDRESS)
