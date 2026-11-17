Cream = []
CreamColor = ["White", "Yellow", "Blue", "Purple"]

while True:
    wha = input("Do you know what cream is? (Yes/No) ---> ")
    if wha.lower() == 'yes':
        print("Pick one mate? (View the list)")
        for x in CreamColor:
            print(x)#Show list to people
        yeah = input("Which one would you like? ----> ")
        print(yeah, "is a great choice!")
        co = input("Is pink a nice color? (Yes/No)")
        CreamColor.append("Pink")
        for x in CreamColor:
                        print(x)#Show list to people
        break
    else:
        print("Thanks")
        print("You have encoded this:")
        for x in CreamColor:
                print(x)#Show list to people
        break

        