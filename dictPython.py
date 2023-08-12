dic = {key: value for key, value in [('name', 'Test'), ('number', 69)]}
print(dic)
print(type(dic))

# Khởi tạo dict rỗng
dic = dict()
print(dic)

# Khởi tạo dict từ 1 mapping object
# class Map_Class:
# 	def key(self):
# 		return [1, 2,3]
# 	def __getitem__(self, key):
# 		return key * 2
# map_obj = Map_Class()
# dic = dict(map_obj)
# dic
# print(dic)

# Khởi tạo dict từ iterable
iter_ = [('name', 'Test'), ('number', 69)]
dic = dict(iter_)
print(dic)
print(type(dic))

# Khởi tạo bằng keyword arguments
name = 'Test'
member = 123123
dic = dict(name='123', member='test')
print(dic)
print(type(dic))

# Lấy value trong Dict bằng key
iter_ = ('name', 'number', 69, True)
dic = dict.fromkeys(iter_, 'Test')
print(dic['number'])

# Thay đổi nội dung của Dict
iter_ = ('name', 'number', 69, True)
dic = dict.fromkeys(iter_, 'Test')
dic['abc'] = 'Python'
print(dic)
print(dic['abc'])

dic = dict(K=123, T='Test', C='Code')
print(dic)
dic['K'] = dic['K'] + 1
print(dic)
dic['T'] = dic['T'] + ' - Abc'
print(dic)

# Copy
d = {'Test':'ABC', (1,2): 123}
print(d)
d1 = d.copy()
print(d1)

# Clear
d.clear()
print(d)

# Get
d = {'Test':'ABC', (1,2): 123}
value = d.get('Test')
print(value)

# Items
value = d.items()
print(value)

value = list(d.items())
print(value[0][1])

# Keys
value = d.values()
print(value)

# Pop
value = d.pop('Test')
print(value)
print(d)

# PopItem
value = d.popitem()
print(value)
print(d)

# SetDefault
value = d.setdefault('Test')
print(value)
print(d)

value = d.setdefault('Hello Python', 'Bye')
print(value)
print(d)

# Update
d = {'Test':'ABC', (1,2): 123}
print(d)

value = d.update(Test = 'Xyz')
print(value)
print(d)