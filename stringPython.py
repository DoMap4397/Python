a = 'test - TEST'
print(a)
print(type(a))

# HÀm hỗ trợ viết hoa chữ cái đầu tiên
b = a.capitalize()
print(b)

# Hàm hỗ trợ viết hoa tất cả các chữ cái trong chuỗi
c = a.upper()
print(c)

# Hàm hỗ trợ viết thường tất cả các chữ cái trong chuỗi
d = a.lower()
print(d)

# Hàm hỗ trợ viết thường thành viết hoa và ngược lại cho tất cả các chữ cái trong chuỗi
e = a.swapcase()
print(e)

# Hàm hỗ trợ viết hoa tất cả các từ có trong chuỗi
f = a.title()
print(f)

# Căn giữa
g = a.center(40, '*')
print(g)

# Căn phải
h = a.rjust(40, '-')
print(h)

# Căn trái
k = a.ljust(40, '+')
print(k)

# Thay thế 1 ký tự hoặc 1 chuỗi ký tự
j = a.replace('e', 'abc')
print(j)

# Phương thức split
l = a.split()
print(l)

# Phương thức partition
o = a.partition('t')
print(o)

# Phương thức count
t = a.count('t')
print(t)