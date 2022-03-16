# print(), type(), len(), round(), int(), float(), input()

# print() takes unlimited input and return the output
from decimal import ROUND_UP


print(1, '2', True, 'Asabeneh', [1, 1, 2,])
print(type('2'))
print(type([1, 2]))
print(len('cat'))
print(len('cat') ==len('car'))
print(len('Python') == len('Dragon'))
print('Python'.endswith('on') == 'Dragon'.endswith('o'))

print(round(4 / 3, 4))
print(int('2'))
print(float('9.812'))

year_born = input('What year were you born? ')
current_year = 2022
print(type(year_born))

age = current_year - int(year_born)
print(age)



