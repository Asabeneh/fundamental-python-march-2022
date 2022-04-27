empty_set = set()
print(empty_set)
print(len(empty_set))

fruits = {'banana','banana', 'orange', 'mango', 'lemon'}
print(fruits)
print(len(fruits))
fruits.add('avocado')
print(fruits)

for fruit in fruits:
  print(fruit)
  
print('lemon' in fruits)
print('apple' in fruits )
if 'apple' not in fruits:
  fruits.add('apple')
  
print(fruits)

''' fruits.remove('banana')
print(fruits)
fruits.remove('mango')
print(fruits)
fruits.clear()

print(len(fruits))
del fruits
print(fruits) '''

fruits_lst = list(fruits)
print(fruits_lst)

A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
# AUB = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# AnB = {4, 5, 6}
# A\B = {1, 2, 3}
# B\A = {7, 8, 9}
# (AUB)\(AnB) = {1, 2, 3, 7, 8, 9}
print(A.union(B))
print(B.union(A))
print(A.intersection(B))
print(B.intersection(A))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.isdisjoint(B))
print(A.issubset(B))

sentence = 'I love Python. It is the best programming language. But JavaScript is more important than any other programming languages. Do you agree?'
word_lst = sentence.lower().replace('.', '').replace('?', '').split()
print(len(word_lst), word_lst)
words_st = set(word_lst)
print(len(words_st), words_st)