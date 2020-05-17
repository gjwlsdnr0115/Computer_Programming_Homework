def modCount(n, m):
    """
    Returns how many numbers between 1 and n are evenly divisible by m
    :param n: input n
    :param m: input m (m <= n)
    :param count: the count of numbers that are evenly divisible
    :return: how many numbers between 1 and n are evenly divisible by m
    """
    count = 0
    for i in range(2, n):
        if i % m == 0:
            count += 1
    return count

