



user_name = input("Please enter your user name: ")
password = input("Now please enter your password: ")
age = int(input("Now please enter your age: "))
if user_name == "Alirezakhandehjam":
    print("User name is correct", "✔")
else:
    print("User name is not correct", "❌")
if password == "hamine":
    print("Also your password is correct", "✔")
else:
    print("Oops, your password is not correct", "❌")
if 18 < age <= 90:
    if 18 < age <= 50:
        print("You are allowed to enter", "✔")
    else:
        print("Damn, you look younger", "😉")
else:
    print("You are not old enough or too old to enter", "😂")
# Final check
if user_name == "Alirezakhandehjam" and password == "hamine" and 18 < age <= 50:
    print("Access granted! Welcome 🎉")
else:
    print("Access denied! ❌")
