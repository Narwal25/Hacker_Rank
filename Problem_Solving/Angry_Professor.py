def angryProfessor(k, a):
    number = 0
    for i in a:
        if i <= 0:
            number += 1
            
    return "YES" if k > number else "NO"
