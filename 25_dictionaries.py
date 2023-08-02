##
dic1 = {"name":"Vyankatesh",
    "age": 24,
    121:"Andhale"
}

print(dic1["name"])
# accessing single value
print(dic1.get("age"))
# accessing Multipl Values
print(dic1.values())

## key -Values pair

print(dic1.items())
for key,value in dic1.items():
    print(f"the key {key} And value {value}")