"""
lst = [1, 2, 3]
print('Number of items in the list:', len(lst), lst)
# Append mehtod to add an item
lst.append(4)
lst.append(100)
lst.append('Milk')
lst.append(200)
lst.extend([7, 8, 9, 10])
print('Number of items in the list:', len(lst), lst)

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num1_2 = num1 + num2
print(num1_2)
 """


from numpy import number


nums = [1, 2, 3]

print('Number of items in the list:', len(nums), nums)
nums.insert(1, 9.81)
print('Number of items in the list:', len(nums), nums)
nums.insert(3, 3.14)
print('Number of items in the list:', len(nums), nums)
nums.insert(0, 'item 1')
print('Number of items in the list:', len(nums), nums)

countries = ['Finland','Sweden','Denmark','Iceland','Norway']
print('Number of items in the list:', len(countries), countries)
countries.pop() # without an argument it remove the last item
countries.pop(2) # remove the item with corrosponding index
print('Number of items in the list:', len(countries), countries)

countries = ['Finland','Sweden','Denmark','Iceland','Norway']
print('Number of items in the list:', len(countries), countries)
# let modify this countries list using remove

countries.remove('Iceland')
print('Number of items in the list:', len(countries), countries)

# del

countries = ['Finland','Sweden','Denmark','Iceland','Norway']
print('Number of items in the list:', len(countries), countries)
del countries[1:3]
print('Number of items in the list:', len(countries), countries)

# Reverse list
countries = ['Finland','Sweden','Denmark','Iceland','Norway']
print('Number of items in the list:', len(countries), countries)
countries.reverse()

print('Number of items in the list:', len(countries), countries)
# sort
countries = ['Finland','Sweden','Denmark','Iceland','Norway']
print('Number of items in the list:', len(countries), countries)
countries.sort(reverse=True)
print('Number of items in the list:', len(countries), countries)
numbers = [9.81, 3.14, 2.27, 100, 6.23]
numbers.sort(reverse=True)
print(numbers)

# sorted builtin function
countries = ['Finland','Sweden','Denmark','Iceland','Norway']
print('Number of items in the list:', len(countries), countries)
copy_of_countries = countries.copy()
sorted_countries = sorted(countries)
print('Number of items in the list:', len(countries), countries)
print(sorted_countries)
# Notice the difference between sort method and sorted builtin function

copy_of_countries.append('Marsland')
print(countries)

print('Finland' in countries)

if 'Norway' in countries:
  print('The index of finland is ', countries.index('Norway'))
else:
  print('Estonia is not in the list')

