a = int(input("Size? ----> "))
l = 1
for e in range(a):
    for n in range(e + 1):
        if l <= a:
            print(l , end= " ")
            l = l + 1
    print() 