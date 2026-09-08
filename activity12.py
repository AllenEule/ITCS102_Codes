#conditional thing
import getpass
print("Conditional/Statements")
Name = "Beel"
Password = "Kalpas"

e = input("Enter Your Username ---->   ")
u = getpass.getpass("Enter Your Password ---->   ")

if Name == e and Password == u :
	print("Access Granted")
else:
	print("Access Denied")

