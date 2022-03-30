# What are strings?
# A string is a text any data under a single, double, triple quote can be considered as a string
# how long is a string, it a single character or many many pages


from itertools import count


letter = 'a'
print(len(letter))
word = 'python'
print(word, len(word))
sentence = 'Python is great'
print(sentence, len(sentence))

words = sentence.split()
print(len(words))

first_name = 'Asabeneh'
print(first_name.lower())
print(first_name.upper())

# split(), lower, upper(), count(), starswith(), endswith(), title(), swapcase()
print('land' in 'Finland')
print('Tea' in ['Milk','Potatop','Tea','Sugar'])

country  = 'Finland'
print(country.startswith('Fin'))
print(country.endswith('land'))

first_name = 'Asabeneh'
last_name = 'Yetyeh'
age = 250
country = 'Finland'
city = 'Helsinki'
full_name = first_name + ' ' +  last_name

print(full_name)

print('My name is ' + full_name + '. ' + 'I live in ' + city + ', ' + country + '. ' + 'I am ' + str(age) + ' years old.')

print(f'My name is {full_name}. I live in {city}, {country}. I am {age} years old.')

# My name is Asabeneh Yetayeh. I live in Helsinki, Finland. I am 250 years old. 

a = 4
b = 3
print(f'The sum of {a} and {b} is {a + b}')
print('The sum of {} and {} is {}'.format(a, b, a + b))
print(f'The difference of {a} and {b} is {a - b}')
print(f'The product of {a} and {b} is {a * b}')
print(f'The division of {a} and {b} is {a / b :.3f}')
print(f'The modules of {a} and {b} is {a % b}')
print(f'The floor division of {a} and {b} is {a // b}')
print(f'The power of {a} and {b} is {a ** b}')

word = 'Python'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
last_index = len(word) - 1
print(word[last_index])

print(word[-1])
print(word[-2])
print(word[4] == word[-2])
print(word[1:])
print(word[0:2])
print(word[2:])
print(word[-4:])