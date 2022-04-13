lst = [1, 2, 3, 4, 5]
print(len(lst), lst)
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])

last_index = len(lst) - 1
print('The last index is:', last_index)
print('The last item is:', lst[last_index])
print('The last item is ', lst[-1])
print(lst[-2])

# Slicing:start index and ending index but it does not include the item of the ending index
print(lst[1:4])
print(lst[2:4])
print(lst[3:])
print(lst[-4:-2])
