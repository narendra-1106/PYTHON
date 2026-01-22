
def func1():

    try:
        l=[1,2,5,6]
        i=int(input("Enter a Number :"))
        print(l(i))
        return 1
    except:
        print("Error occured ")
        return 0
    finally:
        print("Code executed")

x=func1()
print(x)