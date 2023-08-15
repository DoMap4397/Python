class Test:
	supper = 100
	def __init__(self, para_ten, para_tuoi, para_mau_sac):
		self.ten = para_ten
		self.tuoi = para_tuoi
		self.mau_sac = para_mau_sac 

class TestAbc(Test):
	def __init__(self, para_ten, para_tuoi, para_mau_sac, para_them):
		super().__init__(para_ten, para_tuoi, para_mau_sac)
		self.them = para_them

# Kế thừa hàm constructor
Test_1 = TestAbc('oop_class_inherit', '020', 'Blu', 'Thêm giá trị mới ở thằng con')
print(Test_1.__dict__)
print(Test_1.supper)