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

def are_last_x_elements_same(lst,x):
    lst_2 = []
    if len(lst) < x:
        return False
    if len(lst) >= x:
        lst.reverse()
        for i in range(0,x):
            l = lst[i]
            if l not in lst_2 and len(lst_2) != 0:
                return False
            else:
                lst_2.append(l)
    return True