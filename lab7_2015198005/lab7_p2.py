def ordered3(int_1, int_2, int_3):
    """
    Checks if the passed three integers are ordered from smalles to largest
    :param int_1: first integer
    :param int_2: second integer
    :param int_3: third integer
    :return: True if all integers are ordered, otherwise return False
    """
    if (int_1 <= int_2) and (int_2 <= int_3):
        return True
    else:
        return False