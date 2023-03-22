# Find The way with map
# Write a python program to triple of all numbers of a given list of integers,use python map.
# Sample numbers :[1, 2, 3, 4, 5, 6, 7]
# Triple of  all numbers :
#[3, 6, 9, 12, 15, 18, 21]


nums = (1, 2, 3, 4, 5, 6, 7 )

print("sample num : ", nums)

result = list (map(lambda x : x + x + x, nums))

print("Triple of list numbers: ") 

print(list(result))

