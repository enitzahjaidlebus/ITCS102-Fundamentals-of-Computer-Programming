print("Welcome to the manga Reader Recommender!")
print("What Genre Would You like to Pick?")
genre = input("[Action,Romance,Isekai]: ").lower()

if genre == "Action".lower():
    print ("You Have Selected", genre)
    print ("How long would You Like?")
    duration = input("[Long,Medium,Short]: ")

    if duration == "Long".lower():
        print("You have Picked", duration)
        print("What Year Would You Like?")
        year = input("[2000,2010]: ")

        if year == "2000":
            print("You Have Selected", year)
            print("We Recommend One Piece")
        elif year == "2010":
            print("You Have Selected", year)
            print("We Recommend Attack on Titan")#SBJ

    elif duration == "Medium".lower():
            print("You have Picked", duration)
            print("What Year Would You Like?")
            year = input("[2000,2010]: ")
            if year == "2000":
                print("You Have Selected", year)
                print("We Recommend Dogs: Bullets & Carnage")
            elif year == "2010":
                print("You Have Selected", year)
                print("We Recommend Akudama Drive")

    elif duration == "Short".lower():
            print("You have Picked", duration)
            print("What Year Would You Like?")
            year = input("[2000,2010]: ")
            if year == "2000":
                print("You Have Selected", year)
                print("We Recommend Alive")
            elif year == "2010":
                print("You Have Selected", year)
                print("We Recommend Destroy and Revolution")

elif genre == "Romance".lower():
    print ("You Have Selected", genre)
    print ("How long would You Like?")
    duration = input("[Long,Medium,Short]: ")

    if duration == "Long".lower():
        print("You have Picked", duration)
        print("What Year Would You Like?")
        year = input("[2000,2010]: ")

        if year == "2000":
            print("You Have Selected", year)
            print("We Recommend Fruits Basket")
        elif year == "2010":
            print("You Have Selected", year)
            print("We Recommend Nisekoi")

    elif duration == "Medium".lower():
            print("You have Picked", duration)
            print("What Year Would You Like?")#JBS
            year = input("[2000,2010]: ")
            if year == "2000":
                print("You Have Selected", year)
                print("We Recommend Paradise Kiss")
            elif year == "2010":
                print("You Have Selected", year)
                print("We Recommend Horimiya")

    elif duration == "Short".lower():
            print("You have Picked", duration)
            print("What Year Would You Like?")
            year = input("[2000,2010]: ")
            if year == "2000":
                print("You Have Selected", year)
                print("We Recommend Solanin")
            elif year == "2010":
                print("You Have Selected", year)
                print("We Recommend I Want to Eat Your Pancreas")


if genre == "Isekai".lower():
    print ("You Have Selected", genre)
    print ("How long would You Like?")
    duration = input("[Long,Medium,Short]: ")

    if duration == "Long".lower():
        print("You have Picked", duration)
        print("What Year Would You Like?")
        year = input("[2000,2010]: ")

        if year == "2000":
            print("You Have Selected", year)
            print("We Recommend Sword Art Online")
        elif year == "2010":
            print("You Have Selected", year)
            print("We Recommend That Time I Got Reincarnated as a Slime ")

    elif duration == "Medium".lower():
            print("You have Picked", duration)
            print("What Year Would You Like?")
            year = input("[2000,2010]: ")
            if year == "2000":
                print("You Have Selected", year)
                print("We Recommend Fushigi Yuugi: Genbu Kaiden")
            elif year == "2010":
                print("You Have Selected", year)
                print("We Recommend Re:Zero")

    elif duration == "Short".lower():
            print("You have Picked", duration)
            print("What Year Would You Like?")
            year = input("[2000,2010]: ")
            if year == "2000":
                print("You Have Selected", year)
                print("We Recommend The Twelve Kingdoms")
            elif year == "2010":
                print("You Have Selected", year)
                print("We Recommend The Rising of the Shield Hero")

#Hell po
