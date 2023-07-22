def get_elem_from_list(list_,elem_):
    for l in list_:
        if elem_ in l:
            return (l)
    return ("")

def get_elem_from_list_special(list_,elem_):
    i = 0
    for l in list_:
        if elem_ in l:
            i = i + 1
            if i == 2:
                return (l)
    return ("")