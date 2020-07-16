def resetValues(L, threshold):
    """
    creates new list with elements 0 if it is above the threshold
    :param L: input list
    :param threshold: threshold value
    :return: Result list
    """
    Result = [] #result list
    for num in L:
        if num > threshold:     #if element above threshold
            Result.append(0)    #append 0
        else:
            Result.append(num)  #else, append element
    return Result
