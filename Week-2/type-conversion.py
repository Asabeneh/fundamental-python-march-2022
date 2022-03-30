num_int = 2
print(num_int, type(num_int))
num_str = str(num_int)
print(type(num_str))

num_str = '10'
print(num_str, type(num_str))
num_int = int(num_str)
print(num_int, type(num_int))

gravity_str  = '9.81'
print(gravity_str, type(gravity_str))

gravity_num = float(gravity_str)
print(gravity_num, type(gravity_num))

print(str(2) == '2')
print(2 == int('2'))
print(float(2) == float('2'))

test = '9.81'
print(int(float(test)))

