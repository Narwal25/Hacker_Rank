def circularArrayRotation(a, k, queries):
    result = []
    k = k % len(a)
    a = a[-k:] + a[:-k]
    for i in queries:
        result.append(a[i])
    return result
