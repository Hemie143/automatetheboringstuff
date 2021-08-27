import imapclient
import pyzmail

imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')     # 'my_email_address@example.com Jane Doe authenticated (Success)'

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2019'])
print(UIDs)                                 # [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]

rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
print(message.get_subject())                # 'Hello!'
print(message.get_addresses('from'))        # [('Edward Snowden', 'esnowden@nsa.gov')]
print(message.get_addresses('to'))          # [('Jane Doe', 'jdoe@example.com')]
print(message.get_addresses('cc'))          # []
print(message.get_addresses('bcc'))         # []
print(message.text_part != None)            # True
print(message.text_part.get_payload().decode(message.text_part.charset))        # 'Follow the money.\r\n\r\n-Ed\r\n'
print(message.html_part != None)            # True
print(message.html_part.get_payload().decode(message.html_part.charset))        # '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al<br></div>\r\n'
imapObj.logout()
