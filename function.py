def f(test=[]):
	test.append('T')
	print(test)

f()
f()
f()
f()

def Test(t, e, s, a):
	print(t)
	print(e, s)
	print('end', a)

lst = ['123', 'Test', 69.96]
Test(*lst, a = 'Kết thúc')

def abc(*args):
	print(args)
	print(type(args))
# Unpack sau đó pack
abc(*(x for x in range(5)))


def test(name, member):
	print('name =>', name)
	print('member =>', member)
dic = {'name': 'Python', 'member': 123}
test(**dic)

def say_slogan():
	test = 'Python'
	print('Abc Test', test)
say_slogan()


def make_slogan():
# Khởi tạo với global không có giá trị
	global test
# Sau khi khởi tạo xong, ta mới gán giá trị
	test = 'Python abc'
# Chạy lại hàm
make_slogan()
print(test)

def make_global():
	global x
	x = 1

def local():
	x = 5
	print('x in local', x)

make_global()
print(x)
local()
print(x)

def cal_rec_per(width, height):
	per = (width + height) * 2
	return per

rec_1_width = 5
rec_1_height = 3
# Khởi tạo 1 biến để hứng kết quả
rec_1_per = cal_rec_per(rec_1_width, rec_1_height)
print(rec_1_per)

# Trường hợp này là khi bạn không cần tái sử dụng nó ở lần sau nữa
print(cal_rec_per(7, 4))

# Yield
def square(lst):
	for num in lst:
		yield num **2
test_ret = square([1, 2, 3])
for value in test_ret:
	print(value)