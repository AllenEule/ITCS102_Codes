def my_factorial (In):
    fact = 1
    for x in range(In,0,-1):
        print(x)
        fact *= x
        print(f"factorial of {In} is {fact}")

my_factorial(7)
my_factorial(4)
my_factorial(13)