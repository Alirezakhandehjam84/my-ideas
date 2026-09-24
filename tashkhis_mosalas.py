



side_1 = float(input("please enter side 1: "))
side_2 = float(input("please enter side 2: "))
side_3 = float(input("please enter side 3: "))

if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
    print("sides cannot be zero or negative")

elif (side_1 + side_2 > side_3) and (side_2 + side_3 > side_1) and (side_1 + side_3 > side_2):
    print("this is a triangle")

    if side_1 == side_2 == side_3:
        print("this is an equilateral triangle")

    elif (side_1 == side_2) or (side_1 == side_3) or (side_2 == side_3):
        print("this is an isosceles triangle")

    else:
        print("this is a scalene triangle")

else:
    print("this isn't a triangle")
