print("THE FACTORIAL PROGRAM")

number = eval(input("Enter any number: "))
factor = 1
for x in range(number, 0, -1):
  factor *= x
print("The factorial of", number, "is", factor)