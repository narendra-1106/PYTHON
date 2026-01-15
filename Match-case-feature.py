x=int(input("Enter a value of x :"))
match x:
    case 0:
        print("X is zero")

    case 4:
        print("x is 4")

    case _ if x!=90:
        print(x, " value is not 90")

    case _ if x!=80:
        print(x, "is not 80")

    case _ :  # this _ is used for default num
        print(x)


