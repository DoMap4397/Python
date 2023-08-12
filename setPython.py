set_1 = {69, 96}
print(set_1)
print(type(set_1))

set_2 = {'Test'}
print(set_2)

set_3 = {(69, 'Test'), (1,2,3)}
print(set_3)
# Kiểu set không chứa được hashable

set_4 = {1, 1, 1}
print(set_4)
print(type(set_4))

set_5 = {value for value in range(3)}
print(set_5)

set_6 = set('Test abc')
print(set_6)
# Set không quan tâm đến vị trí các phần tử

print({1, 2, 3, 4} - {1, 2})
print({1, 2} - {1, 2, 3, 4})

print({1, 2, 3, 4} & {1, 2})

print({1, 2, 3, 4} | {1, 2, 5, 6})

print({1, 2, 3, 4} ^ {1, 2})

set1 = {1, 2, 3}
set2 = {3, 4}

set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3

print(set3)
print(set4)
print(set5)