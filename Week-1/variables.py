# variables
# variables are a place to store data
# not allowed to use special characters as variable name except underscore
# you cannot start a variable with a number
# there is shoulb space in a variable naem

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
full_name = first_name + ' ' +  last_name
print(full_name)

print('I am ' + full_name + '.' + 'I am ' + str(age) + ' years old. ' + 'I live in ' + country)
print(f'I am  {full_name}. I am {age} years old. I live in {city}, {country}')


# I am Asabeneh Yetayeh. I am 250 years old. I live in Finland.

a = 4
b = 3

print(f'The sum of {a} and {b} is {a + b}')
print(f'The difference of {a} and {b} is {a - b}')
print(f'The product of {a} and {b} is {a * b}')
print(f'The division of {a} and {b} is {a / b}')
