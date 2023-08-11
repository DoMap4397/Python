a = [i for i in range(30)]
print(a)

# Phương thức count
b = [1,2,3,4,5,1,2,3,1,1]
c = b.count(1)
print(c)

# Phương thức index
d = b.index(5)
print(d)

# Phương thức copy
e = b.copy()
e[0] = 'Test'
print(e)
print(b)

# Phương thức clear
f = b.clear()
print(f)
print(b)

# Phương thức cập nhập
x = [1,2,3]
print(x)
x.append(4)
print(x)

x.append([4,5])
print(x)

x.append([4,5,[6,7]])
print(x)

# Phương thức insert
x.insert(0,9)
print(x)

x.insert(-4,9)
print(x)

# Phương thức pop
x.pop(0)
print(x)

# Phương thức remove
x.remove(1)
x.remove(4)
print(x)

# Phương thức reverse
x.reverse()
print(x)

# Phương thưc sort
x = [1,7,3,9,2]
x.sort()
print(x)