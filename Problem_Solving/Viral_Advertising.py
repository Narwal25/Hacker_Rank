def viralAdvertising(n):
    shown = 5
    liked = 0
    for i in range(n):
        liked += shown//2
        shown = (shown//2)*3
    
    return liked
