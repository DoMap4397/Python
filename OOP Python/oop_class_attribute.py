class Test:
	stt = 1
	so_thu_tu = 1	
	supper = 50

	def __init__(self, para_ten, para_tuoi, para_mau_sac):
		self.ten = 'Python ' + para_ten
		self.tuoi = para_tuoi
		self.mau_sac = para_mau_sac

		self.so_thu_tu = Test.so_thu_tu

		Test.so_thu_tu += 1
		
Test_1 = Test('oop_class_attribute', '000', 'Red')
Test_2 = Test('Test chơi', '010', 'Black')
print(Test.supper)
print(Test_1.supper)

print(Test_1.stt)
print(Test_2.stt)
print(Test.so_thu_tu)