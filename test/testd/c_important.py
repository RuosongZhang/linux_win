numbers = ['abc', 'bnd', 'sdte']
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

zzz = ['abd', 'ccc']
numbers = numbers + zzz
numbers = numbers * 3
print(numbers)

def add_all(t):
    total = 0
    for x in t:
        total += x

    return total
t = [1, 3, 4, 5, 6]
print(add_all(t))

aa = sum(t)
print(aa)


def capotalize_all(x):
    res = []
    for s in x:
        res.append(s.capitalize())

    return res
x = ['asdf', 'bba', 'pwef', 'lskdf']
print(capotalize_all(x))