def patter_print(n):
    for i in range(0,n):
        for j in range(0,i+1):
            if j == i or j == 0:
                print(1, end="")
            else:
                print(2, end="")
        print()

num = int(input("Enter number of rows: "))
patter_print(num)
