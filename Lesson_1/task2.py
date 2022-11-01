frNum=float(input("Enter first number: ")) #User inputs the first number.
secNum=float(input("Enter second number: ")) #User inputs the second number.
oper=input("Choose an operation(+,-,*,/,**,sqrt: ") #Selecting the operation.
if oper=="+":
   res =frNum+secNum
   print("Result:"+ str(res))
elif oper=="-":
    res =frNum-secNum
    print("Result:"+ str(res))
elif oper=="*":
    res =frNum*secNum
    print("Result:"+ str(res))
elif oper=="/":
    res =frNum/secNum            #Calculation and printing of the result.
    print("Result:"+ str(res))
elif oper=="**":
    res =frNum**secNum
    print("Result:"+ str(res))
elif oper=="sqrt":
    import math
    res =math.sqrt(frNum)
    print("Result:"+ str(res))
else: 
    print("You have selected the wrong operation!")