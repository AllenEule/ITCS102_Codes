#task 1
loan = float(input("Enter the loan amount: "))
loanp = int(input("Enter the loan period in years: "))
month = loanp * 12
principal = loan / month
remaining_bal = loan
print("| MONTH |  PAY \t\t|INTEREST\t|PRINCIPAL\t|\tBALANCE\t|")
for x in range(1, month + 1):
    remaining_bal -= principal
    loan_int = remaining_bal * 0.00256
    monthly_pay = loan_int + principal
    print(f"|{x}\t| \t {round(monthly_pay,2)}\t|\t{round(loan_int , 2)}\t|\t{round(principal,2)}\t|\t{round(remaining_bal,2)}\t|")
    #String formatting
