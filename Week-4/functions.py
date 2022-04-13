''' def print_fullname():
  first_name = 'Asabeneh'
  last_name = 'Yetayeh'
  print(first_name, last_name)
  
print_fullname() '''


''' def print_fullname(first_name, last_name):
  print(first_name, last_name)
  
print_fullname('John','Doe')
print_fullname('Asab','Yeta')
print_fullname('Alex','David') '''



def print_fullname(first_name, last_name):
  return first_name + ' ' +  last_name


print(print_fullname('John','Doe'))
print(print_fullname('Asab','Yeta'))
print(print_fullname('Alex','David'))


def add_two_nums(a , b ):
  return a  + b

print(add_two_nums(1, 9))
print(add_two_nums(1, 99))



def make_square(n):
  return n ** 2

print(make_square(3))

# calculate the weight of an object on different planets

def calculate_weight(mass, gravity = 9.81):
  return mass * gravity

print(calculate_weight(75))
print(calculate_weight(65))
print(round(calculate_weight(85, 1.62), 2))