"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab13_p7.py
"""


import os


def searchDir(directory, s):
    """
    Recursively searches 'directory' for .txt files
    that contain string s.
    """

    result = []  # result list
    files = os.listdir(directory)  # get subfiles and subdirectories
    for file in files:
        fullname = directory + '/' + file  # make full name
        if os.path.isdir(fullname):  # is a directory
            result.extend(searchDir(fullname, s))  # recursive call
        else:  # is file
            if os.path.isfile(fullname):
                if fullname[-3:] == 'txt':  # check if file is .txt
                    try:
                        f_txt = open(fullname, 'r')  # open file
                        for line in f_txt:
                            if s in line:  # file conatins string 's'
                                result.append(fullname)  # add to list
                    except OSError:
                        continue  # go to next file
    return result

