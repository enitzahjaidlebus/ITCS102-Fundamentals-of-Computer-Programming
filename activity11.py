temp = eval(input("Enter temperature: "))

if temp <= 0:
    print("Temperature is Below Freezing")
elif temp <= 15:
    print("Temperature is Extremely Cold")
elif temp <= 30:
    print("Temperature is Cold")
elif temp <= 38:
    print("Temperature is Lukewarm")
elif temp <= 42:
    print("Temperature is Warm")
elif temp <= 50:
    print("Temperature is Hot")
elif temp <= 60:
    print("Temperature is Extremely Hot")
else:
    print("Temperature is Burning")