def pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")

        for k in range(1, 2 * i):
            print("*", end="")
        print()


pyramid(5)

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end='')
    print()
