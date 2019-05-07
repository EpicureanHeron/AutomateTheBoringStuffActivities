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

exercise1()

