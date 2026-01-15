x=int(input("Enter a value of x :"))
match x:
    case 0:
        print("X is zero")

    case 4:
        print("x is 4")

    case _:  # this _ is used for default num
        print(x)

