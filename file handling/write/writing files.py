x = open("students.txt", "a")

print(" The file is opened in append mode")

x.write("My name is M.Usama")
x.write("\n I am a Programmer")

x.close()
input("Check the file ,to execute the remaining section press enter")
x=open("students.txt","w")

x.write(" Over written text ")
x.close()