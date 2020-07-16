"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab12_p2.py
"""


def moderateDays(mydict):
    """
    Returns a list [...] of the days for which the average
    temperature was between 70 and 79 degrees.
    :param mydict: dictionary of days and temperature
    :return: list of days with temperature between 70 and 79 degrees
    """
    result = []  # init result list
    for k in mydict.keys():  # iterate through keys
        if mydict[k] >= 70 and mydict[k] <= 79:  # value between 70 and 79
            result.append(k)  # append key to list

    return result  # return list