# Hàm tính giai thừa
def giai_thua(n):
    if n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)


# Hàm tính tổng 2 số
def tong_2_so(a, b):
    t = a + b
    return t
