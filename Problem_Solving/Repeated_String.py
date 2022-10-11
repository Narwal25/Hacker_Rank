def repeatedString(s, n):
    count = s.count('a') * (n//len(s))
    count += s[:n%len(s)].count('a')
    
    return count
