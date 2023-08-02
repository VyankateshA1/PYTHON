# Factorial

def factorial(n):
    if(n==0) or (n==1):
        return 1
    else:
        return(n * factorial(n-1))
    
print(factorial(5))


# Fibonacci
def fibinacci(n):
    num1 = 0
    num2 = 1
    num3 = num1 + num2
    return num3

print(fibinacci(5))