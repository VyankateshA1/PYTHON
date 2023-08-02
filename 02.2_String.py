# String Methods
#upper()
str = "vyan"
print(str.upper())

#lower()
str = "VYAN!!!!!@@"
print(str.lower())
print(str.rstrip("!@"))

#replace()
str1 = "Vyan"
print(str1.replace("Vyan","Andh"))

#split()
str2 = "Vyakatesh Andhale"
print(str2.split(" "))

#capitalize()
str = "hello how are you"
print(str.capitalize())

#centre()
str = "Good Morning!"
print(str.center(20))

'''We can also provide padding character to the centre() method'''
print(str.center(20,"."))

#count()
str = "hello"
print(str.count("l"))

#endswith()
str = "have a nice day"
print(str.endswith("day"))

'''We can also check with start and end index of String'''
print(str.endswith("a",1,6))

#find()
str = "hey how are you"
print(str.find("are"))
print(str.find("arer"))#return -1

#indes()
str = "good day"
#print(str.index("hey"))

#isalnum()
str = "WelcomeToTheProgramming"
print(str.isalnum())

#isalpha()
str = "Welcome"
print(str.isalpha())

#islower()
str = "hello"
print(str.islower())

#isprintable()
str = "how are you"
str1 = "how are you\n"
print(str.isprintable())
print(str1.isprintable()) # \n cant printable it return false

#isspace()
str = "   "
str1 = "hello"
print(str.isspace())
print(str1.isspace())

#istitle()
str = "How Are You"
print(str.istitle())

#isupper()
str = "HELLO FRIENDS"
print(str.isupper())

#startswith()
str = "have a good day"
print(str.startswith("have"))

#swapcase()
str = "hello guys"
str1 = "HELLO GUYS"
print(str1.swapcase())

#title()
str = "have a good day"
print(str.title())
