#logical operator

A = 23
L = 23
Name = "Allen"
Last_Name = "Eule"


print(A > L)
print(not(A > L and A < L))
print(A > L and Name == "Allen")
print(A < L or Name == "Allen" and Last_Name == "Eule")
print(A <= L and Last_Name == "Eule" or Name == "Franzen")
print(not(L >= A and Last_Name == "Eule" or Name == "Allen"))

