emp= { 
    1 : 45 ,
    2 : 30 ,
    3 : 80 ,
    4 : 40     
}
emp2= { 
    225 : 90,
    251 : 91
}

emp.update(emp2)
# emp.clear()  for clear full dictionary
# emp.pop(225) delete only 1 key value pair
# emp.popitem()   for deleting last value of dictionary

# del emp[3]  deleting one item used del 

print(emp)