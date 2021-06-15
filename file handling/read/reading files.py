x = open("students.txt", "r")
if x.readable():
    print("File is readable")
else:
    print("File is not readable")
# print("TO read every information in the file using read function : ",x.read())
# print("the first line of the file using readline function : ",x.readline())
# print("\n All lines in file using readlines function : ", x.readlines())

# as readlines store the lines in index , the line can be indivdually called as following

# print("Individual line using readlines ,first line :", x.readlines()[0])

print(" Using For loop reading the file")

for line in x.readlines():
    print(line)
x.close()
"""
for line in x.read():
    print(line)
x.close()
"""
