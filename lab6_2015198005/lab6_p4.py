words = []      #initialize word list

more = True
while more:     #more input
    word = input('Enter a word (q to quit): ')
    if(word == 'q'):    #if q, stop
        more = False
    else:
        ch = word[0].lower()    #make word lower-case
        check = word[1:]    #check rest of the word
        if ch in check:     #if first letter is in rest of the word
            words.append(word)

words.sort()    #sort list
print(words)