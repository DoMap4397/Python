giatriA = input()
giatriB = input()
try:
    soA = float(giatriA)
    soB = int(giatriB)
except:
    print('ĐỊnh dạng đàu vào không hợp lệ!!!')
# Dùng format thì làm tròn cả những số thừa sẽ thành số 0
print('Dùng format: {0:.{1}f}'.format(soA, soB))

# Dùng round thì làm tròn đến số ban đầu được nhập vào
formatedNum = round(soA, soB)
print('Dùng round: ', formatedNum)
