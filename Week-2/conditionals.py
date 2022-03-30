''' a = 5

if a > 0:
  print('a is positive')
else:
  print('Negative')
   '''
  
x = 10
if x > 0:
  print(f'{x} is a postive number')
elif x == 0:
  print(f'{x} is zero')
else:
  print(f'{x} is a negative number')
  
weather = input('What is the weather like? ').lower()
if weather == 'rainy':
  print('Please take a raincoat')
elif weather == 'stormy':
  print('Take care of yourself')
elif weather == 'cloudy':
  print('It might rain')
elif weather == 'sunny':
   print('It is a shiny day and go out freely')
elif weather == 'snowy':
  print('It will be very slippery')
else:
  print('No one knows the weather')
 