s={1,2,5,6}
s2={3,6,7}
print(s.union(s2))
print(s.intersection(s2))

s.update(s2)
print(s,s2)



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
cities4 = cities.intersection(cities2)
print(cities4)

cities3 = cities.difference(cities2)
print(cities3)

print(cities.isdisjoint(cities2))

print(cities.issuperset(cities2))
cities5 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities5))
