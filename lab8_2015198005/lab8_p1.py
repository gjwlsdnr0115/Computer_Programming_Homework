def resetValuesInPlace(L, threshold):
    """
    mutates elements in list to 0 if it is above the threshold
    :param L: list to mutate
    :param threshold: threshold value
    :return: mutated list L
    """
    for k in range(len(L)):
        if L[k] > threshold:    #element bigger than threshold
            L[k] = 0    #mutate to zero
    return L