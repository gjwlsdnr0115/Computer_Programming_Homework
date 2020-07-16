"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab13_p4.py
"""


def fib(n):
    """
    computes the calculation of fibonacci number
    :param n: fibonacci number
    :return: calculation of nth number
    """
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # recursiive call
