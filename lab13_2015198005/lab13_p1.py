"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab13_p1.py
"""


class Range:
    """
    Class to represent a range of integers
    """
    
    def __init__(self, x, y):
        """ Method to construct a Range object """
        # Check that lower bound 'x' is less or equal than upper bound 'y'
        if x > y:
            raise IndexError('lower bound higher than upper bound')
        else:
            self.small = x
            self.big = y

    def __str__(self):
        """ Returns a string representation of the Range object """
        return str(self.small) + '...' + str(self.big)

    def __lt__(self, other):
        """ Returns the boolean result of operator < with two Range objects """
        return self.big < other.small