#obtain an integer
integer=input("Enter an interger: ")
integer=int(integer)
factor=2
#error
if integer<2:
    print("Error")
#determine prime factors
while factor<=integer:
    if integer%factor==0:
        print (factor)
        integer=integer//factor
    else:
        factor=factor+1
