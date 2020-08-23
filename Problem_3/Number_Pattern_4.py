def patter_print(n):
    for i in range(n , 0, -1):
        for j in range(1,i+1):
            print(j, end="")
        print()

num = int(input("Enter number of rows: "))
patter_print(num)
