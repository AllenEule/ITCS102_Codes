from getpass import getpass

allen = False

while allen == False:
    allena = bool(input("Are you Allen? (Yes/No) ------> "))
    yu = bool(input("Are you sure? (Yes/No) ---> "))
    if allena == "Yes" and yu == "Yes":
        print("You in ngl")
        allen = True
    else:
        print("You wrong ngl")
