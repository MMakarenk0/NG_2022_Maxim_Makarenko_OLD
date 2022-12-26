numbers=input("Enter numbers: ") # input numbers (string type).
List=list(numbers.split(", ")) # string distribution and setting the parameter.
List1= list()
maxNum = 0
for number in List:
    List1.append(int(number)) #Filling list int type numbers.
for num1 in List1: #Searching for the biggest number in the list.
    if maxNum<num1:
        maxNum=num1
print("Max number in list is: " + str(maxNum))
List1.remove(maxNum)
minNum = List1[0]
for num2 in List1: #Searching for the smallest number in the list.
    if minNum<num1:
        maxNum=num1
print("Min number in list is: " + str(minNum))
List1.remove(minNum)
sum = 0
for num3 in List1: #Addition of the rest number in the list.
    sum = sum + num3
print("Sum of rest numbers is: " + str(sum))
