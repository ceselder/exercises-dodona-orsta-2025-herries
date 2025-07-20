def vind_naald_indexes(berg):
    return_list = []
    for i, woord in enumerate(berg):
        if woord == "naald":
            return_list.append(i)
    return return_list