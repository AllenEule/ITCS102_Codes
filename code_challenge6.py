a = int(input("Size? ----> "))
l = 0
for e in range(a):
    if l != a:
        for n in range(e + 1):
            if l != a:
                l = l + 1
                print(l , end= "\t")
            elif l == a:
                print("", end="\t")
        print("\n") 
