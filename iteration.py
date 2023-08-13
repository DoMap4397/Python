itera = (x for x in range(3))
print(itera)
print(next(itera))
print(next(itera))
print(next(itera))

# Sum
print(sum(itera, 1))
# khi dùng hàm Sum rồi thì ko thể Next được nữa

# Max
print(itera)
print(max([], default='Test'))
print(max([1,43,64,31,12,4532]))

# Min tương tự như max
print(min([1,43,64,31,12,4532]))

# Sorted
itera=(1,4,6)
print(sorted(itera, reverse=True))
print(sorted(itera))
