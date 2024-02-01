def Compare(a,b):

    if a > b:
        print("a is greater than b")

    elif a == b:
        print("a is equal to b")
    
    else:
        print("b is greater than a")

def main():
    print("Welcome to the Number Comparer!\n")
    a = int(input("Please Enter the first number for comparison:  "))
    b = int(input("Please Enter the second number for comparison:  "))

    Compare(a,b)

    print("Thanks for using the Number Comparer!")

main()