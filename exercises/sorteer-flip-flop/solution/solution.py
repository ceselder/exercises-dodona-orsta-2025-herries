def sorteer_flip_flop(list):
    past = -999999
    flip_flag = True
    for item in list:
        if item < past:
            flip_flag = False
        past = item
    if flip_flag == True:
        return_list = []
        i = len(list)
        while i > 0: # dit kan ook op andere manieren... Maar vind dit het meest begrijpbaar
            i -= 1
            return_list.append(list[i])
        return return_list
    else:
        list.sort()
        return list