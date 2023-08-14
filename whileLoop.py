k = 5
while k > 0:
	print('k = ', k)
	k -= 1

s = 'Test Python'
# Vị trí bắt đầu bạn muốn xử lý của chuỗi
idx = 0
# Lấy độ dài chuỗi làm môc kết thúc
length = len(s)
while idx < length:
    print(idx, 'abc', s[idx])
# Di chuyển index tới vị trí tiếp theo 
    idx += 1
	

five_even_numbers = []
k_number = 1
#Vòng lặp vô hạn vì giá trị này là hằng nên ta không thể kết thúc vòng lặp
while True:
# Nếu k_number là 1 số chẵn
	if k_number % 2 == 0:
# Thêm giá trị của k_number
		five_even_numbers.append(k_number)
# Nếu list này đủ 5 phần tử
		if len(five_even_numbers) >= 5:
# Thì kếu thúc vòng lặp
			break
	k_number += 1
print(five_even_numbers)
print(k_number)

k_number = 0
while k_number < 10:
	k_number += 1
# Nếu k_number là số chẵn
	if k_number % 2 == 0:
		continue
	print(k_number, 'is odd number')
print(k_number)
