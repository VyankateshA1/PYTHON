emp1 = {
    122 : 50,
    123 : 60,
    124 : 55
}

emp2 = {
    201 : 20,
    202 : 30
}

emp2.update({202:60})
emp1.update(emp2)

print(emp1)
### CLEAR() ###
emp1.clear()
print(emp1)

### POP() AND POPITEM()
emp1 = {
    122 : 50,
    123 : 60,
    124 : 55
}
emp1.pop(122)
print(emp1)
emp1.popitem()
print(emp1)

### del-keyword
del emp1
print(emp1)