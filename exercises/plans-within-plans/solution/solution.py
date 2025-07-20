def ontvouw_geneste_tuples(lijst_van_tuples):
    i = 0
    while i < len(lijst_van_tuples):
        current = lijst_van_tuples[i]
        if type(current) is tuple:
            lijst_van_tuples[i:i+1] = list(current)
        else:
            i += 1
    return lijst_van_tuples
