name = input("What is your name? ")
fare = eval(input("How much is your fare? "))
Student = input("Are you a student (yes / no)? ")

if Student.lower() == 'yes' :
	discount = fare * 0.2
	newfare = fare - discount
	print("Hi", name)
	print("Your discount is", discount)	
	print("Therefore, your new fare is", newfare)

else:
    print("Sorry,", name,", you are not a student thats why you're not eligible for a discount")
    print("Therefore, your fare is still ", fare)#jbs