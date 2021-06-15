from Parent import parent
from child import child

print("-------------------The parent class----------------------- ")
pr = parent()
pr.eye_colour()
pr.height()

print("\n -------------------The child class-----------------")
ch = child()
ch.eye_colour()  # inherited feature
ch.height()
