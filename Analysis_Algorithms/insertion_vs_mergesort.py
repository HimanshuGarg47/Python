import math

n = 2
while True:
    if n < 8 * math.log2(n):
        print("for n = " + str(n) + ", insertion sort beats merge sort")
    else:
        print("for n = " + str(n) + ", merge sort wins!")
        break
    n += 1