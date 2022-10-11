def beautifulDays(i, j, k):
    count = 0
    for num in range(i,j+1):
        re = int(str(num)[::-1])
        if not abs(num-re) % k:
            count += 1
    return count
