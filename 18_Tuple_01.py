### Operation on Tuples ###

countries = ("INDIA","USA","CANADA")
print(countries)
#chnage tupule into list
countries = list(countries)
print(countries)
#ADD ITEM
countries.append("RUSSIA")
print(countries)
#REMOVE ITEM
countries.pop(1)
print(countries)
#CONVERT INTO TUPLE AGAIN
countries = tuple(countries)
print(countries) 


### WE CAN CONCATENATE TWO TUPLES 

one = (1,2,3)
two = (4,5,6)
join = one + two
print(join)


### Count() METHOD 

tuples = (1,2,3,3,4,55,55,6,1,3,3,1)
count=tuples.count(3)
print("Total count is:", count)

### Index() METHOD


tuples = (1,2,3,3,4,55,55,6,1,3,3,1)
count=tuples.index(3)
print("index of 3 is:",count)

#occurance in given Range
count=tuples.index(3,8,10)
print("Occurance In Given Range of index 3 is:",count)

#Length() METHOD

count = len(tuples)
print(count)