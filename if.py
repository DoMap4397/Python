a = 0
b = 3
if a -1 < 0:
	print('a nhỏ hơn 1')
if b -1<0:
	print('b nhỏ hơn 1')

a = 0
b = -6
if a -1 < 0:
	print('a nhỏ hơn 1')
if b -1<0:
	print('b nhỏ hơn 1')

a = 0
b = 3
if a -1 < 0:
	print('a nhỏ hơn 1')
	if b - 1 < 0:
		print('b nhỏ hơn 1')

a = 3
# False, tiếp tục
if a - 1 < 0:
	print('a nhỏ hơn 1')
# False, tiếp tục
elif a - 2 < 0:
	print('a nhỏ hơn 2')
# False, tiếp tục
elif a - 3 < 0:
	print('a nhỏ hơn 3')
# False, tiếp tục
elif a - 4 < 0:
	print('a nhỏ hơn 4')
# Khối BIG đã kết thúc, dù đây là True nhưng không ý ngĩa
elif a - 5 < 0:
	print('a nhỏ hơn 5')

a = 3
# False, tiếp tục
if a - 1 < 0:
	print('a nhỏ hơn 1')
# Else
else:
	print('a nhỏ hơn 5')