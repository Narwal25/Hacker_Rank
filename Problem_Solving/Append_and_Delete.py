def appendAndDelete(s, t, k):
    match = 0
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            break
        match += 1
    if k > len(s) + len(t):
        return "Yes"
    if (len(s) + len(t) - match*2) <= k and (k - len(s) - len(t) + match*2) % 2 == 0:
        return "Yes"
    return "No"
