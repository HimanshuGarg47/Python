def countSpecialNumbers(N, arr):
    count_freq = dict()

    max_ele = max(arr)
    special = [False for i in range(0, max_ele + 1)]

    for x in arr:
        # print(x, count_freq)
        if x in count_freq:
            count_freq[x] +=1 
            continue
        for i in range(2 * x, max_ele+1, x):
            special[i] = True
        
        count_freq[x] = 1

    # Print all special numbers
    count = 0
    for p in arr:
        if special[p] or (p in count_freq and count_freq[p]>1):
            count += 1
            # print(p, end=" ")

    return count


arr = [2, 3, 6, 10, 13, 15, 44, 55, 66, 99]
print(countSpecialNumbers(10, arr))
