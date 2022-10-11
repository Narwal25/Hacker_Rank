def climbingLeaderboard(ranked, player):
    result = []
    ranked = sorted(set(ranked), reverse=True)
    for i in player:
        low = 0
        high = len(ranked)
        

        while (low < high):
            mid = (low + high) >> 1            
            if (ranked[mid] > i):
                 low = mid + 1
            else:
                 high = mid
            
        result.append(low+1)
        
    return result
