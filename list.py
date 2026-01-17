l=[3,4,5]
print(l)
print(type(l))

marks=[3,4,5,"Narendra", "Naru"]  #allows string,bollean
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
# print(marks[3])
print(marks[-2])
print(marks[len(marks)-2]) #negative to positive
print(marks[1])

if 7 in marks:
    print("yes")
else:
    print("no")

if "Narendra" in marks:
    print("yes")
else:
    print("no")

if "rendra" in "Narendra":
    print("yes")
else:
    print("no")



print(marks)
print( marks[:])
print(marks[0:5:2])
print(marks[0:-1])
# print(marks[0:4])
print(marks[0:4:2])

lst=[i for i in range(4)]
print(lst)