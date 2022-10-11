def findDigits(n):
    count = 0
    for i in str(n):
        if i != "0" and not (n % int(i)) :
            count += 1
    return count
