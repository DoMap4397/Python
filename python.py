length = 3
iter_ = (x for x in range(length))
c = 0
while c < length:
	print(next(iter_))
	c += 1


s = 'Test Python'
for ch in s:
	if ch == '':
		continue
	else:
		print(ch)