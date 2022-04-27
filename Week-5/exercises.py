nums = [1, 2, 3, 9.81, 3.14]

def sort_numbers_by_type(lst):
  integers = []
  float_nums = []
  for n in lst:
    if type(n) == int:
      integers.append(n)
    else:
      float_nums.append(n)
  # return intergers, float_nums
  return {
		'floats':float_nums,
  'integers':integers
	}

print(sort_numbers_by_type(nums))
      