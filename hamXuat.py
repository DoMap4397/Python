# Sep
print('Test', 'Python', 'abc')
print('Test', 'Python', 'abc', sep='---')

# End
print('line1')
print('line2')
print('line3')
print('Test Python', end='')
print('Test Python', end='***')
print('time')

#Nhập hàm sleep từ thư viện time
from time import sleep

# Dừng chương trình 3 giây
print('stat...')
sleep(3)
print('end...')

#In ra nội dung và kết thúc bởi 1 chuỗi rỗng
print('start...', end='')
# Dừng chương trình 3 giây
sleep(3)
print('end...')

print('line1\n', 'line2', end='')
print('end')

# With
with open('fileText.tst', 'w') as f:
	print('Test', file=f)

your_name = 'Python'
your_grreat = 'Hello! My name is '
for c in your_grreat + your_name:
	print(c, end='', flush=True)
	sleep(0.1)
print()