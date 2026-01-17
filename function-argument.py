# int(input("Enter a first no: " ))
# int(input("Enter a second no: " ))


def average(a,b):
    print("average is: ", (a+b)/2)

# a= int(input("Enter a first no: " ))
# b= int(input("Enter a second no: " ))

average(8,2)


def name(fname, mname = "Uttamkumar", lname = "Jagtap"):    #fname= first name
    print("Hello,", fname, mname, lname)                    #mname= middle name
                                                            #lname= last name
name("Narendra")

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is : ", sum/len(numbers))

average(5,5)
average(10,6,4,34,34)
average(1,2,3,4,5,6,7,8,8)


