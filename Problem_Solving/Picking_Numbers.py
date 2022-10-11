def pickingNumbers(a):
    a = sorted(a)
    max_count = count = 1
    last = a[0]
    for i in range(1,len(a)):
        if a[i] - last > 1:
            last = a[i]
            count = 1
            continue
        else:
            count += 1
            max_count = max(max_count, count)
    return max_count

# def pickingNumbers(a):
#     max_count = 1
#     for i in set(sorted(a)):
#         max_count = max(a.count(i) + a.count(i+1), max_count)
#     return max_count
