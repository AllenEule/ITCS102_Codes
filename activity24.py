Ice_w = {"Sweet":"Cream","Long":"Candy","Small":"Cube","Big":"Block"}
Ice = ["Cream", "Candy", "Cube", "Block"]

#Print
print(Ice)
print(Ice_w)
print(Ice[2])
print(Ice_w["Big"])

#Dictionary Traversing
for x, y in Ice_w.items():
    print("It is", x, "<------> It's", y)
