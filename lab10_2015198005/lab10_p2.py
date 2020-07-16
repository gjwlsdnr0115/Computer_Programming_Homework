def copyFiles(f1, f2, f3):
    '''
    Copies content of the first and second file onto the third file
    :param f1: first file name
    :param f2: second file name
    :param f3: third file name
    :return: 0
    '''
    #open read files
    file1 = open(f1, 'r')
    file2 = open(f2, 'r')
    #open write file
    file3  = open(f3, 'w')

    #init string variable to copy contents
    s = ''

    #copy contents to string 's'
    for line in file1:
        s += line
    for line in file2:
        s += line

    #write 's' on the thrid file
    file3.write(s)

    return 0
