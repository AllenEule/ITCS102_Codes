#Reviewer for finals


age = int(input("what is your age mate ----> "))
revenue = float(input("what is your revenue -----> "))
credit = int(input("what your credit mate ---> "))
years = float(input("how many years your business ----> "))
defaults = bool(input("filed for brankrupcy? (True/False) ------> "))
colN = input("What is the name of collateral? ---> ")
colV = float(input("What value is your collateral? ------> "))

maxloan = 0
basefee = 0


#Baseline #TIER 1
if age >= 21 and years >= 2.0 and defaults == False:
    print("You are eligitible")
    if credit >= 720: #1
        maxloan = 3 * revenue
        print("Eligitible")
        if revenue >= 50000:
            basefee = maxloan * 0.015
            print("Your loan limit is" ,basefee)
        else:
            basefee = maxloan * 0.025
            print("Your loan limit is",basefee)
        if colV >= maxloan:
            print("Accepted")
        else:
            print("Rejected")
        if colV % 5000 !=0:
            basefee += 250
            print("Additional charge base fee", basefee)
        else:
            print("Collateral value is divisible by 5000")


    elif credit <= 620 and credit < 720: #2
        print("Eligitible")
        maxloan = revenue * 1.5
        if years >= 5.0:
            basefee = maxloan * 0.02
            print("Your business has a", basefee)
        else:
            basefee = maxloan * 0.035
            print("Your business has a", basefee)
        if colV >= maxloan:
            print("Accepted")
        else:
            print("Rejected")
        if colV % 5000 !=0:
            basefee += 250
            print("Additional charge base fee", basefee)
        else:
            print("Collateral value is divisible by 5000")

    elif credit < 620:
        print("REJECTED")
    else:
        print("REJECTED") 

else: 
    print("Rejected")
