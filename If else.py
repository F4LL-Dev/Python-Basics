def ty():
    print("thanks for visiting x.Y.Z bank")


# ty function was just created to print such line as it is using at various stages is optional*
print("Welcome to the Bank ")
print("----------Processing Account Information-----------")
a = input("Enter your name :")
b = int(input("Enter your age :"))
if b >= 18:
    print("The Account for " + a + " is legible")
    ty()
elif b >= 10 and b <= 17:
    print("You are not legible for the Business Account")
    print("Child Savings Account can be created")
    print("Please reply Y for Yes or N for No to make a Child Savings Account")
    x = input("Y or N :")
    if x == "Y" or x == "y":
        print("The child account for the " + a + " can be created")
        ty()
    else:
        print("Options Declined")
        ty()
else:
    print("You are not legible for the account")
    ty()
