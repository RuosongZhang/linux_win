num_list = [1,3,5,2,3]

print(num_list[0:2])

print(sorted(num_list))

num_list_2 = [8,4,2,5,7,3]

print(sorted(num_list_2,reverse=True))

num = []
for num_list , num_list_2 in zip(num,str):
    print(num_list_2,'is',num_list)