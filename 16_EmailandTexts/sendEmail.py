import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

smtpObj.ehlo()

smtpObj.starttls()

pw = input('input password: ')

smtpObj.login('<email address>', pw)

smtpObj.sendmail('<email address>', '<recipient address', 'Subject: testing!. \nI am testing this out')

# The start of the email body string must begin with 'Subject: \n' for the subject line of the email. The '\n' newline character
#      separates the subject line from the main body of the email.


smtpObj.quit()