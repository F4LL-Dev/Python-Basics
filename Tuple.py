Tuple_coordinates = (4, 2)
print(Tuple_coordinates)
print("the x coordinates is " + str(Tuple_coordinates[0]) + " \n Y cooridnate is " + str(Tuple_coordinates[-1]))

list_tuples = [(2, 3), (3, 2), (1, 1)]
# list_tuples.sort()
print(list_tuples)

# new
tuple1 = (1,3,2, 2)
tuple2 = (2, (1, 3))
print(f'addition : {tuple1 + tuple2}')

print("inner tupple 2nd element : ", tuple2[1][1])

sorted_tuple1=sorted(tuple1)
print("New Sorted tuple as tuple is immutable :",sorted_tuple1)