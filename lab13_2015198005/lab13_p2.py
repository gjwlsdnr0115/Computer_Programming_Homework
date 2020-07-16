"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab13_p2.py
"""


class AvgList(list):
    """
    Class to compute average of numeric types in list
    """

    def computeAvg(self):
        """
        Computes the average of a list of numeric types.
        Raises the ValueError exception if a list element is neither
        an instance of an 'int' nor a 'float' class.
        :return: average of numeric types in list
        """

        sum = 0
        for i in range(len(self)):
            if isinstance(self[i], int) or isinstance(self[i], float):
                sum += self[i]
            else:
                raise ValueError
        return sum / len((self))