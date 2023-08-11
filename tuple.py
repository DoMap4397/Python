tup = (1,2,(3,56),'Test',76,342)
print(tup)

tup = (i for i in range(10) if i % 2 == 0)
print(tup)

a = tuple([1,2,3])
print(a)
b = tuple('Test')
print(b)
c = tuple(tup)
print(c)

d = a + (2,5,7)
print(d)

e = a * 2
print(e)

f = a[2]
print(f)

g = len(a)
print(g)