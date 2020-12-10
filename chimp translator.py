def translator(phrase):
    translator = ""
    for x in phrase:
        if x in "AEIOUaeiou":
            translator=translator + "m"
        else:
            translator = translator + x
    return translator


y = input("Enter the phrase :")
z = translator(y)
print("The Phrase In Chimps Language is Following :")
print(z)

# print(translator(input("Enter the Phase"))
