def jumpingOnClouds(c, k):
    energy = 99 - c[0]*2
    i = (k) % len(c)
    while i:
        energy -= 1 + c[i]*2
        i = (i + k) % len(c)
    
    return energy
