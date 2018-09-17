def double(l):
    l.extend(l)
    return l

a = [1,2,3]
b = double(a)
print(a)
print(b)