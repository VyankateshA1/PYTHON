
###### EXAMPLE - 1

a = input("Enter the num :  ")
print(f"Multiplication Table of {a} ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(f"Invalid Input!!! {a}")
    
print("End of Programm")
print("have nice day")


#### EXAMPLE - 2

# try:
#     num = int(input("give integer"))
#     a = [6,3]
#     print(a[num])2
# except ValueError:
#     print(ValueError)
# except IndexError:
#     print(IndexError)