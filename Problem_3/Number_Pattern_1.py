def pattern_print(n:
    for i in range(1, n+1):
        for j in range(i):
            print(1,end="")
        print()

number = int(input("Enter number of rows: "))
pattern_print(number)
