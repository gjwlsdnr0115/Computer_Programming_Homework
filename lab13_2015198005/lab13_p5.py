"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab13_p5.py
"""


fib_nums = {}  # global dictionary


def fib_memo(n):
    """Computes the n-th Fibonacci number using memorization."""

    if n in fib_nums:  # 'n' in dictionary
        return fib_nums[n]  # return value in dictionary
    else:  # not in dictionary
        if n == 0:  # base case
            fib = 0
            fib_nums[n] = fib  # add fibonacci number to dictionary
            return fib  # return number
        elif n == 1:  # base case
            fib = 1
            fib_nums[n] = fib  # add fibonacci number to dictionary
            return fib  # return number
        else:  # recursive case
            fib = fib_memo(n - 1) + fib_memo(n - 2)  # compute fibonacci number
            fib_nums[n] = fib  # add number to dictionary
            return fib  # return number
