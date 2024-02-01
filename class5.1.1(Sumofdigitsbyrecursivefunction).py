'''
#EX. of Recursive function
####Sum of digits :-
n=int(input("Enter the number: "))
def sumDigit(n):
    if n==0:
        return 0
    return (n%10)+sumDigit(n//10)
print(sumDigit(n))
'''
