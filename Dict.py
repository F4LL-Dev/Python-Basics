Days_Dictionary = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday"
}

print("Getting the key definition for Mon: " +Days_Dictionary["Mon"])
print("getting the key definition using 2nd method as for Mona : "+Days_Dictionary.get("Mona","No matched"))


Chapters={
1:"Basics Of Computer Languages",
2:"Language Translators",
3:"Comparison Of Various Languages"
}

x=int(input("Input the Number :"))
if x==1:
    print(Chapters[1])
elif x==2:
    print(Chapters[2])
elif x==3:
    print(Chapters[3])
else :
    print("Wrong Input , There are only 3 Chapters ,Input 1-3")
