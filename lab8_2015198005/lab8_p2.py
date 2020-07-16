def removeValuesInPlace(L, threshold):
    """
    removes elements in list that are above threshold
    :param L: list to mutate
    :param threshold: threshold value
    :return: mutated list L
    """
    del_list = []   #list to contain elements to delete
    for num in L:
        if num > threshold:
            del_list.append(num)    #append element to del_list
    for num in del_list:
        L.remove(num)   #remove elements that are in del_list
    return L