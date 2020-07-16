"""
Name: Jinwook Huh
Student ID: 2015198005
Lab problem: lab12_p3.py
"""


import random
import sys

# user input
f_name = input('Enter a filename: ')

# generate file names
name = f_name[:-3]
txt_file_name = name + 'txt'
key_file_name = name + 'key'
encrypt_file_name = name + 'enc'

# if input was .txt file
if f_name[-3:] == 'txt':
    try:
        txt_file = open(f_name, 'r')  # open file
    except FileNotFoundError:
        print('File not found.')
        sys.exit(0)  # terminate program

    # open key file
    key_file = open(key_file_name, 'w')

    # list of characters for encryption
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

    encrypt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

    for c in chars:
        e = random.choice(encrypt)  # get random value

        while(e == c):  # 'c' is encrypted as itself
            e = random.choice(encrypt)  # pick again

        encrypt.remove(e)  # remove value to avoid multiple keys
        key_file.write(c + ',' + e + '\n')

    # close file
    key_file.close()

    # open .key file to start encryption
    keys = open(key_file_name, 'r')

    # make dictionary of keys
    keys_dict = {}
    for line in keys:
        line = line.replace('\n', '')
        l = line.split(',')
        keys_dict[l[0]] = l[1]

    # open encrypted file
    encrypt_file = open(encrypt_file_name, 'w')

    # read through .txt file and write in .enc file
    for line in txt_file:
        for c in line:
            if c != '\n':  # do not encrypt '\n'
                encrypt_file.write(keys_dict[c])
            else:
                encrypt_file.write('\n')
    encrypt_file.close()  # close file

# input is .enc file
else:
    try:
        encrypt_file = open(encrypt_file_name, 'r')
        keys = open(key_file_name, 'r')
    except FileNotFoundError:  # file not found error
        print('File not found.')
        sys.exit(0)  # terminate program

    # make reversed dictionary of keys
    keys_dict = {}
    for line in keys:
        line = line.replace('\n', '')
        l = line.split(',')
        keys_dict[l[1]] = l[0]  # reverse keys and values

    # open .txt file
    txt_file = open(txt_file_name, 'w')

    # read through .enc file and write
    for line in encrypt_file:
        for c in line:
            if c != '\n':
                txt_file.write(keys_dict[c])
            else:
                txt_file.write('\n')
    # close file
    txt_file.close()

