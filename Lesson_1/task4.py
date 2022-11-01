import math

a=float(input('Enter "a" for quadratic equation: ')) 
b=float(input('Enter "b" for quadratic equation: ')) #Inputs of the coefficients.
c=float(input('Enter "c" for quadratic equation: '))
discrim=(b**2)-(4*a*c) #Formula of the discriminant.
x1=(-b-math.sqrt(discrim))/(2*a)    #Formulas of the roots of quadratic equation. 
x2=(-b+math.sqrt(discrim))/(2*a)
print(f"First root: {x1}, second one: {x2}") #Output to the console.