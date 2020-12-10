students = ["usama", "Akbar", "Saleem", "Ali", ]

print("all elements " + str(students))
print("specific index element " + students[0])
print("2nd last stored Element " + students[-2])
print("all elements after 1 ", students[1:])

print("all elements after usama excluding ali ", students[0:3])

students[1] = "Aslam"
print("Ali replaced to Aslam", students)

#new

Rollnumber="A1,A2,A3,A4"
lis1=Rollnumber.split(",")
print(lis1)

print("print the type ",type(students[1]))