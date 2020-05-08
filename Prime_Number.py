def prime_number(n):
    #Determines if number is greter or less than 1
    if n<=1:
        print("False")
    #Determines if the number is prime or not
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
#Prime number inputted
number=int(input("Enter a number: "))
output=prime_number(number)

#Output statement
if output == False:
    print("The number is not prime")
else:
    print("The number is prime")
