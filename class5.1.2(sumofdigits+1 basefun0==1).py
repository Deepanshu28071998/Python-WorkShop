
#EX2. sum of all digits with base function 0==1:
n=int(input("Enter the value: "))
def fun(n):
    if n==0:
        return 1
    if n==2:
        return fun(n-2)
    
    return (n%10)+fun(n//10)
print(fun(n))


