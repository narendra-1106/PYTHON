#strings 
name= "Narendra"
surname= " jagtap"
NJ= '''Narendra
jagtap
age: 18
Narendra jagtap'''

print("Hello ," + name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
# print(name[8]) This gives an error 8th char are not exist

print("\nUsing for loop \n")
for character in NJ:
    print(character)