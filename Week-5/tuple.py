empty_tpl = tuple()
print(empty_tpl)
print(len(empty_tpl))

country_data = ('Finland', 'Helsinki', 'White and Blue', )
print(country_data[0])
print(country_data[-1])

for item in country_data:
  print(item)
  
print('Espoo' in country_data)

print(country_data.index('Helsinki'))

tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
tpl3 = tpl1 + tpl2
print(tpl3)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)

del country_data

print(country_data)