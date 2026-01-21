dic= {
    "Narendra" : "Human",
    "Spoon" : "Object"
}
print(dic["Narendra"])
print(dic.get('Narendra'))

dict= {
    225 : "Narendra",
    2251: "Shreya"
}
print(dict[225])

print(dic)


#Accessing Multiple values


for key in dic.keys():
    print(dic[key])
    print(f"The value is corrosponding to the {key} is {dic[key]}")


print(dic.items())