import sys, pyperclip, re

text = pyperclip.paste()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

emailRegex = re.compile(r'\w+@\w+.\w{,3}')

#phoneNumRegex = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')

mo1 = phoneNumRegex.findall(text)
mo2 = emailRegex.findall(text)

mergedlist = mo1 + mo2

pyperclip.copy(", ".join(mergedlist))