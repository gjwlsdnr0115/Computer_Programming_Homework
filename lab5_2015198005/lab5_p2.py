# sentence input
sentence = input('Enter a sentence: ')
count = 0   #number of vowels in sentence
# upper case
count += sentence.count('A')
count += sentence.count('E')
count += sentence.count('I')
count += sentence.count('O')
count += sentence.count('U')
#lower case
count += sentence.count('a')
count += sentence.count('e')
count += sentence.count('i')
count += sentence.count('o')
count += sentence.count('u')

if(count == 1):  # contains only one vowel
    print('Your sentence contains', count, 'vowel.')
else:
    print('Your sentence contains', count, 'vowels.')