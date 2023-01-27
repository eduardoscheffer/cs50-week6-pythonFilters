from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

for i in range(0, n, 1): # for (let i = 0; i <= n; i++)
    for j in range(0, n, 1): # for (j = 0; j <= n; j++)
        if (i + j < n - 1):
            print(" ", end="")
        else:
            print("#", end="")
    print()