isDirty = True
cycle = 0
while isDirty == True:
    confirm = input("Do you want to continue washing? (yes/no) ").lower()
    cycle += 1
    if confirm == "yes":
        print("Washing Continue... ")
        continue
    else:
        print("Washing Stops...")
        break
print("The number of cycle i", cycle)