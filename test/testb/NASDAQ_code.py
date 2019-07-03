code = {
    'BIDU':'baidu',
    'SINA':'sina',
    'YOUKU': 'Youku'
}
print(code)
a = {'key':123,'key':122}
print(a)

code['YOUKU'] = 'youku'
print(code)

code.update({'FB':'facebook','TB':'tewwle'})
print(code)

del code['TB']
print(code)

letters = ('a','b','c','d')
print(letters[1])

num_list = [1,2,7,8,4,5]

print(sorted(num_list,reverse=True))

a = []
for i in range(1,20):
    a.append(i)
print(a)

b = [i for i in range(1,20)]
print(b)