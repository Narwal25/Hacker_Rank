def squares(a, b):
    count = 0
    na = math.sqrt(a)//1
    if na**2 == a:
        na -= 1
    nb = math.sqrt(b)//1
    
    return int(nb - na)
