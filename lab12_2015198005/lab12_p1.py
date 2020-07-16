"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab12_p1.py
"""


def addDailyTemp(mydict, day, temperature):
    """
    Add key 'day' and value 'temperature' to the dictionary 'mydict',
    only if key 'day' does not already exist in the dictionary.
    The resulting dictionary is returned.
    :param mydict: average temperature dictionary
    :param day: A weekday
    :param temperature: the average temperature of day
    :return: result mydict
    """

    for k in mydict.keys():
        if k == day:  # if key 'day' already exists in mydict
            return mydict  # return mydict

    # key does not exist in mydict
    mydict[day] = temperature  # add key and value to mydict
    return mydict  # return mydict