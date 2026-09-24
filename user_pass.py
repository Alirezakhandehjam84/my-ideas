



user_name = input("please enter your user name:")
password = input("now please enter your password:")
age = int(input("now please enter your age:"))
if user_name == "Alirezakhandehjam" :
    print("user name is correct" , "✔")
else :
    print("user name is not correct" , "❌")
if password == "hamine" :
    print("also your password is correct" , "✔")
else :
    print("Oops your password is not correct" , "❌")
if 18<age<=90 :
    if 18<age<=50 :
        print("you are allow to enter")
    else :
        print("damn you look yonger" , "😉")
else :
        print("you are not old enough or too old to enter" , "😂")
