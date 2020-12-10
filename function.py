def sample_function():
    print("Sample printing")
    print("sample again")


print("not in function")
print("-------function is called")
sample_function()
print("------program ended")


# using parameters
def calc_power(x, y):
    c = pow(x, y)
    print("power of " + str(x) + " is " + str(c))


b = int(input("enter the numer :"))
c = int(input("enter the power of the number to be calculated :"))
calc_power(b, c)





