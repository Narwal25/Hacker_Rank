def acmTeam(topic):
    result = []
    for i, j in combinations(topic, 2):
        result.append(bin(int(i, 2) | int(j, 2)).count("1"))
    result = sorted(result, reverse=True)
    
    return result[0], result.count(result[0])
