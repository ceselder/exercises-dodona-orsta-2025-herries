def tel_groter_dan_vijf(tuple):
    counter = 0
    for x in tuple:
        if x > 5:
            counter += 1
    return counter