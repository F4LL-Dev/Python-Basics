list1=[
    [1,2,3]
    ,
    [2,3,4]
    ,[3,2,3]
]
print("the very first element at row index 0 and column index 0 is ",list1[0][0])

print("========================using for loop=============")
print("all elements :")
for row in list1:
    print(" ",row)

print("So to get the individuals using nest for loop-----------------")
x=0
y=0
for row in list1:
    for column in row:
        print(" Value in row ",x," and column ",y," in the list 1 :",column)
        y+=1
    x+=1
