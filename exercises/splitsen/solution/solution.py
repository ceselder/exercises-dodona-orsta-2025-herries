def groepeer_op_verschil(getallen):
    return_list = []
    curr_list = [getallen[0]]
    oud_verschil = getallen[1] - getallen[0]
    for i in range(1,len(getallen)):
        nieuw_verschil = getallen[i] - getallen[i-1]
        if nieuw_verschil != oud_verschil: #oude lijst toevoegen, nieuwe maken en oud_verschil aanpassen
            return_list.append(curr_list)
            curr_list = [getallen[i]]
            oud_verschil = nieuw_verschil
        else:
            curr_list.append(getallen[i]) #blijven gaan
    return_list.append(curr_list) 