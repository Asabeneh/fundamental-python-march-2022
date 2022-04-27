''' 
empty_dct = {}
print(type(empty_dct))
finnish_english_dct = {
"talo":"house",
 "opiskelija":"student",
 "koulu":"school",
 "kirja":"book",
 "kirjasto":"library",
 "sana":'word',
 "sanasto":"dictionary"
}
print(finnish_english_dct)
print(len(finnish_english_dct))
keys = finnish_english_dct.keys()
print(keys)
values = finnish_english_dct.values()
print(values)
items = finnish_english_dct.items()
print(items)
for item in items:
  print('The meaning of ', item[0],'is ',  item[1]) '''
  
person = {
	'first_name':'Asabeneh',
	'last_name':'Yetayeh',
	'country':'Finland',
	'gender':'male',
  'age':250,
  'is_married':True,
  'skills':['HTML','CSS','JS','TS','Python','Node'],
  'address':{
		'city':'Espoo',
  	'zipcode':'02770',
	  'street_name':'space_street'
	}
}
print(person)
print(person['first_name'])
print(person['last_name'])

if 'nationality' in person:
  print(person['nationality'])
else:
  person['nationality'] = 'Ethipian'
  
# We can use .get() method if we are not sure the key exists in the dictionary
# Sometimes it is good to check if the key exist in the dictionary

person['skills'].append('MYSQL')
print(person)
print(person['skills'][-3])

print(person)

person['hobbies'] = ['Running', 'Ice Skating', 'Jogging']
person.pop('age')
print(person)

keys = person.keys()
print(keys)
values = person.values()
print(values)
items = person.items()
print(items)
person_copied = person.copy()
person_copied['qualification'] = 'Software Engineer'
print(person_copied)

