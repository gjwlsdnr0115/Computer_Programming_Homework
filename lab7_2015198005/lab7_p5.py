isbn = input('Enter an ISBN: ')     #input isbn
groups = isbn.split('-')            #split string into list by '-'

print(groups[0] + '.'*(20-len(groups[0])) + 'GS1 prefix')       #print output with a fieldwidth of 20 characters
print(groups[1] + '.'*(20-len(groups[1])) + 'Group identifier')
print(groups[2] + '.'*(20-len(groups[2])) + 'Publisher code')
print(groups[3] + '.'*(20-len(groups[3])) + 'Item number')
print(groups[4] + '.'*(20-len(groups[4])) + 'Check digit')