def saveThePrisoner(n, m, s):
    pos = (m + s - 1) % n
    return pos if pos else n
