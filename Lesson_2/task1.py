userInput = input("Enter string: ")
letterCounts = {}
sortedLetterCounts = {}
uniqueSymbols = set(userInput)
for unique in uniqueSymbols:
    letterCounts[unique] = userInput.count(unique)
print (letterCounts)
print("===============================")
List = list()
sortedList = list()
for unique1 in uniqueSymbols:
    List.append(unique1)
List.sort()
sortedList.extend(List)
for sortedUnique in sortedList:
    sortedLetterCounts[sortedUnique] = userInput.count(sortedUnique)
print (sortedLetterCounts)
print("===============================")
valueList = list()
valueSet = set(letterCounts.values())
for unique2 in valueSet:
    valueList.append(unique2)
valueList.sort(reverse=True)
for value in valueList:
    keys = {i for i in letterCounts if letterCounts[i] == value} 
    print(str(keys) + ":" + str(value))
