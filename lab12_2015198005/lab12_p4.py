"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab12_p4.py
"""


class Fraction(object):
    """
    Class to represent a number as a fraction

    Examples: 1/2, 2/5
    """

    def __init__(self, n, d):
        """ Method to construct a Fraction object """
        # Check that n and d are of type int:
        if type(n) != int or type(d) != int:
            raise ValueError('requires type int')
        # Check that denominator is non-zero:
        if d == 0:
            raise ZeroDivisionError('requires non-zero denominator')
        # If we get here, n and d are ok => initialize Fraction:
        self.num = n
        self.denom = d
        self.reduce()  # use reduce fraction when newly creating

    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)

    def __mul__(self, other):
        """ Returns new Fraction representing self * other """
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """ Returns new Fraction representing self + other """
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return Fraction(new_num, new_denom)

    def __float__(self):
        """ Returns a float-value of the Fraction object """
        return self.num / self.denom  # result of / is of type float

    def reduce(self):
        """
        Reduces self to simplest terms. This is done by dividing both
        numerator and denominator by their greatest common divisor (GCD).
        Also removes the signs if both numerator and denominator are
        negative. Whole numbers (1, 2, ...) are represented as
        1/1, 2/1, 3/1, ...
        """

        # if both nominator and denominator are negative values, remove signs
        if self.num < 0 and self.denom < 0:
            self.num = self.num * -1
            self.denom = self.denom * -1

        # get greatest common divisor
        x = self.num
        y = self.denom
        gcd = 0

        # get smaller number
        if x > y:
            small = y
        else:
            small = x

        # compute gcd
        for i in range(1, small + 1):
            if ((x % i == 0) and (y % i == 0)):
                gcd = i

        # divide both nominator and denominator with gcd
        # convert type into int
        self.num = int(self.num / gcd)
        self.denom = int(self.denom / gcd)

    def adjust(self, factor):
        """Multiplies numerator and denominator by factor."""
        self.num = self.num * factor
        self.denom = self.denom * factor


