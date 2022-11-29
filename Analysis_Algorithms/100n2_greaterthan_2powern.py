import math

n = 1
while True:
    if (100 * n * n) < (2 ** n):
        print(f"100*n*n is {100*n*n} < 2**n is {2**n}")
        print(n)
        break
    n += 1