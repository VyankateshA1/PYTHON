#
#Default Arguments
#
# def average(a=10,b=10):
#     print("The average is :",(a+b/2))
    
# average()
#we can Override default value
#average(b=55)
#average(22,55)

#
#Keyword Arguments
#
# def average(a=10,b=10):
#      print("The average is :",(a+b/2))
    
# average(b=5,a=10)

#
#Required Arguments
# #
# def average(a,b=10):
#      print("The average is :",(a+b/2))
    
# average(a=5)

#
#Variable-Length Argument
#

#Arbitrary Argument (*)

#example-1
# def arbitrary (*num):
#      sum = 0
#      for i in num:
#           sum += i
#      print(sum/len(num))
          
# arbitrary(5,6)

#example-2

def name(*name):
     print("hello", name[0],name[1])

name("vyan","Andh")
          