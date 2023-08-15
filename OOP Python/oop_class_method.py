class Abc:
	supper = 50
	def __init__(self, para_ten, para_tuoi, para_mau_sac):
		self.ten = para_ten
		self.tuoi = para_tuoi
		self.mau_sac = para_mau_sac
	@classmethod
# Thường những phương thức xử lí thế này hay có tên là from... 
	def from_string(cls, s):
		lst = s.split('-')
		new_lst = [st.strip() for st in lst]
		ten, tuoi, mau_sac = new_lst
		return cls(ten, tuoi, mau_sac)
infor_str = 'oop_class_method - 000 - Red'
Test = Abc.from_string(infor_str)
print(Test.__dict__)

class xyz:
	supper = 100
	def __init__(self, para_ten, para_tuoi, para_mau_sac):
		self.ten = para_ten
		self.tuoi = para_tuoi
		self.mau_sac = para_mau_sac
	@staticmethod
# Nếu không dùng staticmethod thì phải thêm self vào xuat_hien(self)
	def xuat_hien():
		print('1..2..3 ==> Xuất hiện dòng chữ...')
xyz_1 = xyz('oop_class_method', '010', 'Black')
xyz_1.xuat_hien()