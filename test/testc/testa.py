other = {'city': 'beijing', 'habit':'program'}

def personinfo(name, number, **kw):
    print('name:',name, 'xuehao:', number, 'other:', kw)

personinfo('xiaozhi',1002,city=other['city'], habit=other['habit'], yy=other['city'])
personinfo('xiaozhi',1002, **other)