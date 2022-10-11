def jumpingOnClouds(c):
    jump = 0
    i = 0
    while i < len(c) - 1:
        if (i + 2) <= len(c) - 1 and c[i+2]:
            i += 1
        else:
            i += 2
        jump += 1
        
        
    return jump
        
