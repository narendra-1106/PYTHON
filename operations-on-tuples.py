countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
res1 = Tuple1.index(3)
res2 = Tuple1.index(3 , 4, 8)
res3= len(Tuple1)
print('Count of 3 in Tuple1 is:', res)
print('Count of 3 in Tuple1 is:', res1)
print('Count of 3 in Tuple1 is:', res2)
print('Length of Tuple1 is:', res3)
