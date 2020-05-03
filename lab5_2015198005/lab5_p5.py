# initialize variables
name_list = []
count = 0   # number of 'a's

# variable to stop while loop

more = True
while(more):
    name = input('Enter a name (q to quit): ')
    if(name == 'q'):    # user quit input
        more = False
    else:
        name_list.append(name)

for name in name_list:
    count += name.count('a')
    count += name.count('A')

print("Appearance of letter 'a':", count)
