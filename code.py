print(3 > 1)
print(1 < 0)
print(12 == 10 + 2)
print((5*0) != 0)
print('Test' == "Test")
print('Test' == 'abc')
print(ord('A'))
print(ord('a'))
print('a' > 'A')

# is
lst = [1, 2, 3]
lst_ = [1, 2, 3]
print(lst == lst_)
print(lst is lst_)

_lst = lst
print(lst)
print(_lst)
print(id(lst))
print(id(_lst))
print(lst is _lst)

# NOT, AND và OR
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

# Số 0, None, Rỗng
print(bool(0))
print(bool(None))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool({}))

print(bool(1))
print(bool('abc'))
print(bool([1, 2, 3]))

# 1 là True, 0 là False
print(True + 1)
print(False +1)
print(int(True))
print(int(False))

# Syntaxnic sugar cho việc so sánh trong Python
k = 4
print(k in (3, 4, 5))
