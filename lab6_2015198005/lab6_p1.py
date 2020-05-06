name = input('Enter a first and last name: ')   #input name
first_name = name.split()[0]    #allocate first and last name
last_name = name.split()[1]

full_name = last_name + ', ' + first_name[0] + '.'  #make full name string
print(full_name)
