people=30
cars=40
trucks=15

if cars>people:
    print("we should take the cars")
elif cars<people:
    print("we should not take the cars")
else:
    print("everyone should take the cars")
if trucks>cars:
    print("we should buy trucks")
elif trucks<cars:
    print("we should sell trucks")
else:
    print("everyone should buy trucks")
if people>trucks:
    print("we should sell people")
else:
    print("everyone should sell people")