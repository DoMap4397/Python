class Test:
	pass
# Test_1 chính là 1 object thuộc lớp Test
Test_1 = Test()
print(Test_1)

Test_1.ten = 'Test Python'
Test_1.bai = 'Class'
Test_1.abc = '123'

print('Tên của ngôn ngữ là: ', Test_1.ten)
print('Tên của bài học là: ', Test_1.bai)
print('Test số chơi: ', Test_1.abc)
print('?@!: ', Test_1.abc)

# Hàm constructor (initialize method)
class Test:
    def __init__(self, para_ten, para_bai, para_abc):
        self.ten = 'ABC ' + para_ten
        self.bai = para_bai
        self.abc = para_abc

    def xin_chao(self):
    	return 'Xin chào, ta chính là: ' + self.ten
Test_1 = Test('Test Python', 'Class', '123')

print('Tên của test là: ', Test_1.ten)
print('Tên của test là: ', Test_1.bai)
print('Tên của test là: ', Test_1.abc)
# Vì nó là hàm nên nhớ thêm () để gọi hàm
print(Test_1.xin_chao())
# Một cách gọi khác nhưng rất không phổ biến
print(Test.xin_chao(Test_1))