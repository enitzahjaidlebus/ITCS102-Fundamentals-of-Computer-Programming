name = input("Enter your name: ")
print("_____________________________________________")
print("ODD NUMBER SUMMATION PROGRAM, press 0 to stop.\n")

con = True
summation = 0
odd = " "
while con == True:
    number = eval(input(f"Enter a random number, {name}: "))
    if number == 0:
        con = False
        print("Program ended.")
        break
    elif number % 2 == 1:
        summation += number
        odd += str(number) + " "
        continue
    else:
        print("Invalid input!")
        continue

print(f"\nHello {name}, the sum of odd numbers is: {summation}")
print(f"List of odd numbers:{odd}")