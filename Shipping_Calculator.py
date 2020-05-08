
def shipping_calculor(n):
    return (10.95+2.95*(n-1))

#number of items inputted
number=int(input("The number of items: "))
print("For",number,"items,the shipping cost will be $",shipping_calculor(number))
