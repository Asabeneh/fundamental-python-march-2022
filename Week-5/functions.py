def add_two_number(a, b):
  return a + b

print(add_two_number(1, 2))

def make_square(n):
  return n ** 2

print(make_square(5))
print(make_square(10))
print(make_square(-4))
countries = ['Finland','Sweden','Denmark','Iceland','Norway']
def change_list_item_to_uppercase(lst):
  new_lst = []
  for item in lst:
    new_lst.append(item.upper())
  return new_lst

print(change_list_item_to_uppercase(countries))
print(change_list_item_to_uppercase(['Banana','Mango','Coffee','Milk']))

def sum_all_nums(n):
  total = 0
  for i in range(n+1):
    total = total + i
  return total

print(sum_all_nums(3)) #6
print(sum_all_nums(10)) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(sum_all_nums(1000))