### list
#list1 = [1,2,3,"VYAN",True,False]
# print(list1)

# ###
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# print(list1[5])

#### CHECK IF ITEM IS PRESENT IN THE LIST

# if "VYAN" in list1:
#     print("Name is present")
# else:
#     print("Name is not present")
    
# if "YAN" in "VYANKATESH":
#     print("YES")

### RANGE OF INDEX
# list1 = [1,2,3,"VYAN",True,False]
# print(list1[1:2])

### LIST COMPREHENSION

List2 = [i for i in range(10)]
print(List2)
List2 = [i for i in range(10) if i%2==0]
print(List2)


####

list3 = ["Vyan","Andh"]
new = [i for i in list3 if "yan" in i]
print(new)

    