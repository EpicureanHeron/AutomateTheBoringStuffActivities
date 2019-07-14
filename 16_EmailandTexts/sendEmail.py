import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

smtpObj.ehlo()

smtpObj.starttls()

pw = input('input password: ')

smtpObj.login('<email address>', pw)

smtpObj.sendmail('<email address>', '<recipient address', 'Subject: testing!. \nI am testing this out')

smtpObj.quit()