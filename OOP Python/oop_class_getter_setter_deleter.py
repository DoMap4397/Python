class Tter:
	def __init__(self, ho, ten):
		self.ho = ho
		self.ten = ten
# Getter
	@property
	def email(self):
		return self.ho + '-' + self.ten + '@Test.com'
	@property
	def ho_va_ten(self):
		return '{} {}'.format(self.ho, self.ten)
# Setter
	@ho_va_ten.setter
	def ho_va_ten(self, ten_moi):
		ho_moi, ten_moi = ten_moi.split(' ')
		self.ho = ho_moi
		self.ten = ten_moi
# Deleter
	@ho_va_ten.deleter
	def ho_va_ten(self):
		self.ho = None
		self.ten = None
		print('Đã xóa')
Tter_A = Tter('Nguyen', 'Do')
Tter_A.ho_va_ten = 'Abc 123'
print(Tter_A.ho)
print(Tter_A.ten)
print(Tter_A.email)
print(Tter_A.ho_va_ten)
del Tter_A.ho_va_ten
print(Tter_A.ho_va_ten)