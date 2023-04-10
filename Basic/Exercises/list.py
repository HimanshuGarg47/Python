def countSpecialNumbers(N, arr):
    if N <= 1:
        return 0
    arr.sort()

    # remove duplicates and count them
    count_duplicates = 0
    count_freq = {}
    for x in arr:
        if x in count_freq:
            count_freq[x] = count_freq[x] + 1
        else:
            count_freq[x] = 1

    for x in count_freq.values():
        if x > 1:
            count_duplicates += x

    special = [True for i in range(arr[-1] + 1)]
    p = arr[0]
    n = arr[N - 1]
    if p == 1:
        p = arr[1]
    while p * p <= n:
        # If special[p] is not
        # changed, then it is a special
        if special[p] == True:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                special[i] = False
        p += 1

    # Print all special numbers
    count = 0
    for p in arr:
        if not special[p]:
            count += 1
            print(p, end=" ")

    count += count_duplicates
    return count


arr = [2, 3, 6, 10, 13, 15, 44, 55, 66, 99]
print(countSpecialNumbers(10, arr))
