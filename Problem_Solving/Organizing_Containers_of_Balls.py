def organizingContainers(container):
    consum, typesum  = [], []
    for i in container:
        consum.append(sum(i))
    for i in zip(*container):
        typesum.append(sum(i))
        
    if sorted(consum) == sorted(typesum):
        return "Possible"
    else:
        return "Impossible"
