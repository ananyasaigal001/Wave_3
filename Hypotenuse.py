# Calculating the hypotenuse
import math
def hypotenuse(a,b):
    c=math.sqrt((a**2)+(b**2))
    return c
#Inputs
a=int(input("Enter the right triangle's first short side length: "))
b=int(input("Enter the right triangle's second short side length: "))

#Computing the inputs and outputting the result
print("The hypotenuse of the right triangle is",hypotenuse(a,b))
