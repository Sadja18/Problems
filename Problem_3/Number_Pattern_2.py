def patter_print(n):
    for i in range(0,n):
        if i == 0:
            num = 1
        else:
            num = i
        for j in range(0,i+1):
            if j == i or j == 0:
                print(num, end="")
            else:
                print(0, end="")
        print()

num = int(input("Enter number of rows: "))
patter_print(num)
