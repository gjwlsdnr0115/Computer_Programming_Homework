"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab13_p6.py
"""


def fibcalls(n):
    """
    Computes the number of function calls required
    to compute the n-th Fibonacci number.
    """

    if n == 0:  # base case
        return 1

    elif n == 1:  # base case
        return 1

    else:  # recursive case
        return 1 + fibcalls(n - 1) + fibcalls(n - 2)  # recursive function call
