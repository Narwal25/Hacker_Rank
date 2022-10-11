def equalizeArray(arr):
    return len(arr) - arr.count(max(set(arr),key = arr.count))
