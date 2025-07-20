def ontvouw_tuples(lijst_van_tuples):
    returner = []
    for local_tuple in lijst_van_tuples:
        if type(local_tuple) is tuple:
            for elem in local_tuple:
                returner.append(elem)
        else:
            returner.append(local_tuple)
    return returner