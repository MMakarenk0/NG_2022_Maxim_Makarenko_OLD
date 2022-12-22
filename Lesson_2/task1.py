userInput = input("Enter string: ")
letterCounts = {}
sortedLetterCounts = {}
uniqueSymbols = set(userInput) #Creating set for unique letter 
for unique in uniqueSymbols:   #Printing count of every letter
    letterCounts[unique] = userInput.count(unique)
print (letterCounts)
print("===============================")
List = list()
sortedList = list()
for unique1 in uniqueSymbols: #Filling list with unique letter for sorting
    List.append(unique1)
List.sort()
sortedList.extend(List)
for sortedUnique in sortedList:
    sortedLetterCounts[sortedUnique] = userInput.count(sortedUnique) #Printing sorted dictionary 
print (sortedLetterCounts)
print("===============================")
valueList = list()
valueSet = set(letterCounts.values()) #Creating set to unique values
for unique2 in valueSet:
    valueList.append(unique2) #Filling list for sorting in descending order
valueList.sort(reverse=True)
for value in valueList:
    keys = {i for i in letterCounts if letterCounts[i] == value} #returns key from value
    print(str(keys) + ":" + str(value)) #Output count of every letter in descending order. And if there is more than 2 keys with the same value - they will be written in one pair of brackets. 
#For example: {a, b}: 4 Instead of a: 4, b: 4.