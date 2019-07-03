a = ['000','0','Null', '002']
if '001' in a or '002' in a:
    print('yes')
else:
    print('no')

abc = {'a':'yyy', 'b':'wer'}
print(a)

# b = str(a)
# print(a)
# print(type(b))
# new = eval(b)
# print(type(new))
# print(new)
#print(b.replace('', ))

bb = []
aa = abc.keys()
print(aa)
print(type(aa))
#aa.sort()
for i in aa:
    print ('%s : %s' % (i,abc[i]))
    bb.append('%s = %s' % (i,abc[i]))
print(bb)
x = '---'.join(bb)
print(x)


