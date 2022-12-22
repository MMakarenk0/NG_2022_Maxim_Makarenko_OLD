num=int(input("Input size: "))

while num>0:
    for el in range(num, 0, -1): #Cicle for printing decrementing numbers
        print(str(el) + " ", end='')
        if el == 1:     #If the number reaches 1 - transfer to a new line
            print("\n")
    num = num-1
    
