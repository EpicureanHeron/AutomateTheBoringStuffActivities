import os
import re

localFiles = os.listdir('./')

regexInput = input("enter regex expression similair to  r'/s/s/s' or some other expression: ")


regexInfo = re.compile(regexInput)

results = []

for f in localFiles:

    contents = open(f, "r+")

    for line in contents:

        mo1 = regexInfo.findall(line)

        if len(mo1) > 0:

            for x in mo1:

                resultFile = f + ', ' + x
                results.append(resultFile)

    contents.close()

print(results)