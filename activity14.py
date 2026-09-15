#if course == bsit
#if isstudent == true
#else:
#if sex == "male"
#elif sex == female
#nested conditions / inside conditions
# Bank loans nested 

age = int(input("What is your age? -----> "))
is_employed = bool(input("Are you employed? (True/False) ----> "))
credit_score = int(input("What is your credit score? -----> "))
annual_income = float(input("What is your annual income? -----> "))
has_collateral = bool(input("Do you have any collateral? (True/False) ----> "))

print("Your age is", age)
print("You are employed?", is_employed)
print("Your Credit Score is", credit_score)
print("You have an annual income of", annual_income)
print("You have collateral?", has_collateral)


if age < 21 and is_employed == 'True':
    print("Applicable")
    if credit_score >= 750:
         print("You have a very high credit score")
         if annual_income >= 10000:
              base_rate3 = 4.5
              print("You have a loyalty discount of", base_rate3)
    else:
              base_rate4 = 5.0
              print("You have a base rate of", base_rate4)
elif 600 <= credit_score and credit_score < 700:
         print("You have a high base rate")
         base_rate1 = 8.0
         print("You have a base rate of", base_rate1)
         if has_collateral == 'True':   
             base_rate2 = 7.0
             print("You have a base rate of", base_rate2)
             if has_collateral =='True' and annual_income < 40000:
                 base_rate = 9.5
                 print("You have a base rate of", base_rate)   
                 if credit_score < 600:
                     print("Rejected: Credit Score is too low")
else:
       print("Rejected: Fails baseline criteria") 