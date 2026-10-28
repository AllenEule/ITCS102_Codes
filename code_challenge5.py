w = int(input("size? ----> "))
for x in range(w):
    for y in range(w):
        if x + y == w-1 or y == x:
            print("*", end= "")
        else:
              print(" ", end="")
    print()