def countLetters(line):
    '''
    Counts the number of letters in the input string and writes it on answer.txt file
    :param line: input string
    :return:
    '''
    count = 0   #initialize count variable to zero
    for c in line:  #iterate through every character in string
        if(c >= 'a' and c <= 'z' ):
            count += 1
        elif(c >= 'A' and c <= 'Z'):
            count += 1
    #make file answer.txt
    myfile = open('answer.txt', 'w')
    #write count
    myfile.write(str(count) + '\n')
