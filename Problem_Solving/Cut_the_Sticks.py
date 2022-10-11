def cutTheSticks(arr):
    result = []
    while arr:
        result.append(len(arr))
        mini, temp = min(arr), []
        for i in arr:
            if i - mini:
                temp.append(i - mini)
        arr = temp
    
    return result
