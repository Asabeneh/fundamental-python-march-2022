# What are the available data types we have in Python?
# Numbers(inter, float, complex), Strings, Booleans(True or False), 
# List
# ['Finland', 'Sweden', 'Denmark', 'Norway','Iceland'] => list
# ('Finland', 'Sweden', 'Denmark', 'Norway','Iceland') => tuple 
# {'Finland', 'Sweden', 'Denmark', 'Norway','Iceland'}
#   {'Finland':'Helsinki', 'Sweden':'Stockholm', 'Denmark':'Copenhagen', 'Norway':'Oslo,'Iceland':'Ry'}
# {'book':'kirja','house':'talo', 'student':'opiskelija'}

# All this are number type data types
print(1, type(1)) # int
print(1.2, type(1.2)) # float
print(10, type(10)) # int
print(9.81, type(9.81)) # float
print(1 + 2j, type(1 + 2j)) # complex number

# Booleans are True or False
print(True, type(True))
print(False, type(False))
print(2 > 1, type(2 > 1))
print(2 < 1, type(2 < 1))
print(2 == 1, type(2 == 1))
print(2 == int('2'))
print(str(2) == '2')

# Strings
print('Asabeneh', type('Asabeneh'))
print('Do you know that I love Python')

# List
print([1, 2, 3, 4], type([1, 2, 3, 4]))
print(['Milk','Meat','Sugar','Coffe'], type(['Milk','Meat','Sugar','Coffe']))

# Tuple

print(('Milk','Meat','Sugar','Coffe'), type(('Milk','Meat','Sugar','Coffe')))

# Set 
print({'Milk','Meat','Sugar','Coffe'}, type({'Milk','Meat','Sugar','Coffe'}))

# Dictionary
print({'book':'kirja','house':'talo', 'student':'opiskelija'}, type({'book':'kirja','house':'talo', 'student':'opiskelija'}))