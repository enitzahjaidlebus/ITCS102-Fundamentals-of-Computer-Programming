print("MULTIPLICATION TABLE MAKER")
number =eval(input("Enter Number: "))
print("\nMultiplication for Table for",number,":")

for x in range(1,11):
    print(number,"x",x,"=",number*x)