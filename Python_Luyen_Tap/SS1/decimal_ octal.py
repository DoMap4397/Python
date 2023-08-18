giatri = input()
isParseDone = False
try:
    sothapphan = int(giatri)
    isParseDone = True
except:
    print('Định dạng đầu vào không hợp lệ!!!')
if isParseDone:
    print('Số thập phân %d trong hệ bát phân là %o' % (sothapphan, sothapphan))