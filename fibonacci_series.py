def fib(n):
    if(n<=1):
        return n
    else:
        return (fib(n-1)+ fib (n-2))
    
# n= int(input("Enter a number : " ))
# print(fib(n))
# print(fib(4))

n= int(input("Enter a number : " ))
for i in range (n):
    print(fib(i) , end ="")


