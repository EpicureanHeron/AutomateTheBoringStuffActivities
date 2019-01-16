# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
#our printTable() function would print the following:


#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

def printTable(listOfLists):
    
    maxList = []

    for x in listOfLists:
        
        maxValue = 0
        i = 0
        for y in x:
            if len(x[i]) > maxValue:
                maxValue = len(x[i])
           # print(len(x[i]))
          #  print(x[i])
            i += 1
        maxList.append(maxValue)
    print(maxList)
printTable(tableData)
        