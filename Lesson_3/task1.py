def output(res):
    print("Result: " + str(res))

def sum(frNum,secNum):
    res =frNum+secNum
    output(res)

def dist(frNum,secNum):
    res =frNum-secNum
    output(res)

def mult(frNum,secNum):
    res =frNum*secNum
    output(res)

def div(frNum,secNum):
    res =frNum/secNum            
    output(res)

def pow(frNum,secNum):
    res =frNum**secNum
    output(res)

def sqrt(frNum):
    import math
    res =math.sqrt(frNum)
    output(res)
    


frNum=float(input("Enter first number: ")) #User inputs the first number.
secNum=float(input("Enter second number: ")) #User inputs the second number.
oper=input("Choose an operation(+,-,*,/,**,sqrt: ") #Selecting the operation.

if oper=="+":
   sum(frNum,secNum)
elif oper=="-":
    dist(frNum,secNum)
elif oper=="*":
    mult(frNum,secNum)
elif oper=="/":
    div(frNum,secNum)
elif oper=="**":
    pow(frNum,secNum)
elif oper=="sqrt":
    sqrt(frNum)
else: 
    print("You have selected the wrong operation!")