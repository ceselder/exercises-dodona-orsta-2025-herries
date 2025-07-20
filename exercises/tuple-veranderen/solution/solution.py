def vervang_element(gegeven_tup, index, new_elem):
    list_gegeven_tup = list(gegeven_tup)
    list_gegeven_tup[index] = new_elem
    print(tuple(list_gegeven_tup))