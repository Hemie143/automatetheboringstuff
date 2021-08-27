import smtplib


smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()                          # (250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
smtpObj.starttls()                      # (220, b'2.0.0 Ready to start TLS')
smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')          # (235, b'2.7.0 Accepted')
smtpObj.sendmail('bob@example.com', 'alice@example.com',
                 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()
