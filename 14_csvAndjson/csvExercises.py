import csv

def exercise1():
    #excercise 1, opening, reading and printing the 
    exampleFile = open('example.csv')
    exampleReader = csv.reader(exampleFile)
    #returns a list of lists
    exampleData = list(exampleReader)
    #prints out each line
    for x in exampleData:
        for y in x:
            print(y)

#exercise1()

def exercise2():
    #writing data to a csv file
    #creates outputFile in write mode
    outputFile = open('output.csv', 'w', newline='')
    #passes file to writer
    outputWriter = csv.writer(outputFile)

    outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])

    outputWriter.writerow(['Hello, world!', 'eggs', 'eggs', 'bacon', 'ham'])

    outputFile.close()

#exercise2()

def exercise3():
    #tsv is a tab sepverated 
    csvFile = open('example.tsv', 'w', newline='')

    csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
    csvWriter.writerow(['apples', 'oranges', 'grapes'])

    csvWriter.writerow(['eggs', 'bacon', 'ham'])

#exercise3()

