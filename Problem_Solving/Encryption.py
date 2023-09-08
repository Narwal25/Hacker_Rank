def encryption(s):
    s = s.replace(" ", '')
    rows = int(math.sqrt(len(s)))
    columns = rows
    
    if rows * columns != len(s):
        columns = rows + 1
    
    if rows * columns < len(s):
        rows = rows + 1
    
    subs = [s[i:i+columns] for i in range(0,len(s), columns)]
    
    newstr = ""
    
    for i in range(columns):
        for sub in subs:
            if len(sub) > i:
                newstr = newstr + sub[i]
        
        newstr = newstr + " "

    return newstr
