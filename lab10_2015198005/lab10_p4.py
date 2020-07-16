#open file 'data.txt'
f = open('data.txt', 'r')

#create list of values in data.txt
og_list = []
for line in f:
    og_list.append(int(line))   #convert to integer

#make edged list with subsituted values
edged_list = [og_list[0]] + og_list + [og_list[-1]]

#init result list
result_list = []
for i in range(1, len(edged_list)-1):
    #compute sliding-window computation
    result_list.append((edged_list[i-1] + edged_list[i] + edged_list[i+1])/3)

#print list
print(result_list)