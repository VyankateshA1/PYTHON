### Joining Sets - union()/update()
## union()
s1 = {1,3,5,9,7}
s2 = {2,4,8,7,6}
print(s1.union(s2))
#update()
s1.update(s2)
print(s1,s2)

#########
# INTERSECTION() AND INTERSECTION_UPDATE()

## intersection()
cities = {"Tokyo","Mumbai","Delhi"}
cities2 = {"Pune","Mumbai","Thane","Tokyo"}
print(cities.intersection(cities2))
cities.intersection_update(cities2)
print(cities)

## Symetric_difference()
### AND
## Symetric_difference_update()
print("##### Symetric_difference() And Symetric_difference_update() #####")
cities1 = {"Tokyo","Mumbai","Delhi","kalyan"}
cities2 = {"Pune","Mumbai","Thane","Tokyo"}
print(cities1.symmetric_difference(cities2))


### difference() AND difference_Update()
print("##### difference() And difference_update() #####")
cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities2 = {"Pune","Mumbai","Thane","Tokyo"}
print(cities.difference(cities2))

### isDisJoint ()
print("##### isdisjoint() #####")
cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities2 = {"Pune","Mumbai","Thane","Tokyo"}
cities3 = {"kk"}
print(cities.isdisjoint(cities2))


### issuperset()
print("##### issuperset() #####")
cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities2 = {"Pune","Mumbai","Thane","Tokyo"}
cities3 = {"Mumbai","Delhi"}
print(cities.issuperset(cities3))

### issubset()
print("##### issubset() #####")

cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities2 = {"Pune","Mumbai","Thane","Tokyo"}
cities3 = {"Mumbai","Delhi"}
print(cities3.issubset(cities))

### add()
print("##### ADD() #####")
cities3 = {"Mumbai","Delhi"}
cities3.add("Kalyan")
print(cities3)

### update()
print("##### UPDATE() #####")


cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities2 = {"Pune","Thane"}
cities.update(cities2)
print(cities)

### remove() And discard()
print("##### REMOVE() AND DISCARD() #####")


cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities.remove("Tokyo")
cities.discard("Mum")

print(cities)
### pop()
print("##### POP() #####")
cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities.pop()
print(cities)

### pop()
# print("##### DEL KEYWORD #####")
# cities = {"Tokyo","Mumbai","Delhi","kalyan"}
# del cities
# print(cities)

### pop()
print("##### CLEAR() #####")
cities = {"Tokyo","Mumbai","Delhi","kalyan"}
cities.clear()
print(cities)




