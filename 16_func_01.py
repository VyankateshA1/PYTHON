#define function 1
def multiple(a,b):
    m = (a*b)
    print(m)
    
    #define function 2
def checkbigger(a, b):
    if(a>b):
        print("a is bigger")
    else:
        print("b is bigger")
        
        #define function empty using Pass for future use - 3
def checksmall(a,b):
    pass


a = 10
b = 20
checkbigger(a,b)
multiple(a,b)