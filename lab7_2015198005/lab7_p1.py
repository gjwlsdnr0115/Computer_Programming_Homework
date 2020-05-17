def zeroCheck(int_1, int_2, int_3):
    """
    Check if any of the input integers are zero
    :param int_1: first integer
    :param int_2: second integer
    :param int_3: third integer
    :return: True if at least one integer is zero, False if none are integers
    """
    if int_1 == 0:
        return True
    elif int_2 == 0:
        return True
    elif int_3 == 0:
        return True
    else:
        return False