def countAllLetters(line):
    '''
    Counts all letters in input 'line' and return list
    :param line: input line
    :return: list of the counts of all letters
    '''
    #convert line into lowercase
    low = line.lower()
    #init count list
    counts = [0]*26
    #create list of all alphabets
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                 'n','o','p','q','r','s','t','u','v','w','x','y','z']
    #init result list
    result = []

    #iterate over all characters in 'low'
    for c in low:
        for a in alphabets:
            if a == c:  #if character is an alphabet
                counts[ord(a)-97] += 1  #increase count of the alphabet

    #interate over all alphabet counts
    for i in range(len(counts)):
        if counts[i] != 0:  #alphabet exists
            result.append((chr(i+97), counts[i]))    #append to result list as tuple

    return result
