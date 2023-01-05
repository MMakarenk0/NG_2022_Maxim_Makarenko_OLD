numbers=input("Enter numbers: ") # input numbers (string type).
List=list(numbers.split(", ")) # string distribution and setting the parameter.
List1= list()
for number in List:
    List1.append(int(number)) #Filling list int type numbers.

maxNum = max(List1)
print("Max number in list is: " + str(maxNum))
List1.remove(maxNum)

minNum = min(List1)
print("Min number in list is: " + str(minNum))
List1.remove(minNum)

sum = 0
for num in List1: #Addition of the rest number in the list.
    sum = sum + num
print("Sum of rest numbers is: " + str(sum))
