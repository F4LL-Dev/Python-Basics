students = ["Usama", "Ali", "Aslam"]
numbers = [1, 3, 32, 3]
students.extend(numbers)
print(students)
students.append(12)
print(students)

students.insert(1, "ahmad")
print(students)

students.remove("ahmad")
print(students)

print("Checking the Value Ali if it is in the list")
print("Checked the value is at ", students.index("Ali"))

print("counting the value appearing in the list as counting how many times is the usama appearing which is :",
      students.count("Usama"))
numbers.sort()
print("the sorted number list", numbers)

numbers.reverse()
print("the reversed list is", numbers)

number2 = numbers.copy()
print("the copied list", number2)

# new
students=[1,2,3]
print("First element is deleted  and returned: ", students.pop(2))
print("First element is deleted but not returned", );
del (students[0])
print("After deletion: ",students)