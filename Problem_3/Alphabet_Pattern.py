def alpha_pattern(n = 4):
    asciiNumber = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            character = chr(asciiNumber)
            print(character, end='')
        print(" ")
        asciiNumber += 1

n = int(input("Enter number of rows: "))
alpha_pattern(n)
