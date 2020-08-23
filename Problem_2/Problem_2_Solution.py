def sum_calculate(num):
    sum_even, sum_odd = 0, 0
    for digit in num:
        if int(digit)%2==0:
            sum_even+=int(digit)
        else:
            sum_odd+=int(digit)

    return str(sum_even) + " " + str(sum_odd)

num = input()
print(sum_calculate(num))
