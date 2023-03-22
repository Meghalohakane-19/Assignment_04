# find the square from the given list 
# write a python program to square the elements of a list using map() function .
# sample list : [4, 5, 2, 9]
# squre the elemets of the list 
# [16, 25, 4, 81]

lst = [4, 5, 2, 9]

print ("original list: ",list)

square_list = list(map(lambda lst: lst**2,lst))

print("squre of the elements of list: ")

print(square_list)