
def shipping_calculator(n):
    return (10.95+2.95*(n-1))

#number of items inputted
number=int(input("The number of items: "))

#Shipment cost
cost=round(shipping_calculator(number),2)
print("For",number,"items,the shipping cost will be $",cost)
