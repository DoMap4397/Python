# In dòng chữ Hello python ra màn hình
print("Hello python")

# Biến (Variable)
a = 1
b = 2.5
s = a + b
ten, tuoi, PI = 'Đô', 27, 3.14

# In biến ra màn hình
print(s)
print(ten)
print(tuoi)
print(PI)

# Kiểm tra kiểu
print(type(ten))
print(type(tuoi))
print(type(PI))

# Lấy toàn bộ nội dung của thư viện decimal
from decimal import*

# Lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 30

f = 10/3
print(f)
print(type(f))

d = Decimal(10)/Decimal(3)
print(d)
print(type(d))

# Lấy toàn bộ nội dung của thư viện fractions
from fractions import*

# In số thập phân
frac = Fraction(6,9)
print(frac)

# Số phức
c = complex(2,5)

print(c)
# In lấy phần số nguyên
print(c.real)
# In lấy phần số ảo
print(c.imag)

# Kiểu chuỗi trong Python
'''
Chuỗi nhiều dòng
'''
str1 ='''
Dòng 1
Dòng 2
Dòng 3
'''
print(str1)

str2="""
Test1
Test2
Test3
"""
print(str2)

#Chuỗi trần
print(r'abc, \nhiều abc')

# Cộng chuỗi
strA = 'abcdef\n'
strB = 'test'
strC = strA + strB
print(strC)
strD = strA*3
print(strD)
strE = strA in strB
print(strE)
strF = strA[0]
print(strF)
strG = strA[-2]
print(strG)
strH = strA[None:None: 2]
print(strH)

# Ép kiểu
str3 = int("10") + 5
print(str3)
str4 = float('1.5') + 1.2
print(str4)
str5 = str(10) + '2'
print(str5)

#Thay thế giá trị trong chuỗi cho sẵn
strB = strB[None:1] + '0' + strB[2:None]
print(strB)

# Tái sử dụng chuỗi
c = 'Test %s %s' %('abc', 123)
print(c)

d = '%s %s'
result = d %(1, 'đô')
print(result)
