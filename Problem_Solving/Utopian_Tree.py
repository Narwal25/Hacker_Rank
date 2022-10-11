def utopianTree(n):
    t = 1
    for i in range( n ):
        if not t % 2:
            t += 1
        else:
            t *= 2
    return t
