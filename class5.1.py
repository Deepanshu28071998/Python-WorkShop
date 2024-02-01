########################## Recursive functions ####################################
#######Recursive functions are function which calls indise the function.
########Recursive functions are functions that calls itself.
########Recursive functions should be terminated with base case .
####INTERNET########Recursive functions are functions that calls itself. It is always made up of 2 portions, the base case and the recursive case. The base case is the condition to stop the recursion. The recursive case is the part where the function calls on itself.



#####EX.syntax:-
'''
def add(a,b):
    add(a,b)
    return add


'''



####Genral syntax:-
'''
def recfun(args.):
    S1
    S2
    recfun(args)
    S3
    recfun(args)
recfun(args)
'''




#EX. of Recursive function
####Sum of digits :-
'''
n=int(input("Enter the number: "))
def sumDigit(n):
    if n==0:
        return 0
    return (n%10)+sumDigit(n//10)
print(sumDigit(n))
'''
#EX2. sum of all digits with base function 0==1:
'''
n=int(input("Enter the value: "))
def fun(n):
    if n==0:
        return 1
    if n==2:
        return fun(n-2)
    
    return (n%10)+fun(n//10)
print(fun(n))
'''


#EX3. multiplication fun with????
'''
n=int(input("Enter the number: "))
def fun(n):
    if n==1 or n==0:
        return 1
    return n*fun(n-1)
print(fun(n))
'''








################################## ANONYMOUS FUNCTION ###################################################
################################################################################################
###########



#EX.
'''

def dob(n):
    return n*2
print(dob(5))
print(dob(9))
'''



#EX. use "LAMBDA"

'''
lambda_dob = lambda n: n*2
print(lambda_dob(5))
print(lambda_dob(9))
'''



#Ex. use of "NAME" function for multiply:
'''
n=int(input("Enter the value: "))
lambda_mul=lambda n:n*5
print(lambda_mul(n))
'''


#EX. use of "NAME" function for multiply with "LAMBDA" function:
'''
n=int(input("Enter the value: "))
def mul(n):
    res=n*5
    return res
print(mul(n))
'''



#EX. use lambda in function
'''
gre=lambda a,b :a if a>b else b
print(gre(8,6))
print(gre(15,32))
'''


#EX. user input for lambda function
'''
gre=lambda a,b : a if a>b else b
a=int(input("a: "))
b=int(input("b: "))
print(gre(a,b))
'''





#EX. Multiple expr with using "LAMBDA" function:
'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
factorial =lambda n:fact(n)
print(factorial(5))
'''



#EX. Multiple expr with using "LAMBDA" function user give the input:
'''
n=int(input("Enter the value: "))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
factorial =lambda n:fact(n)
print(factorial(n))
'''


#EX. circular list create for Multiple expr with using "LAMBDA" function user give the input:
'''
while True:
    n=int(input("Enter the value: "))
    def fact(n):
        if n==0:
            return 1
        return n*fact(n-1)
    factorial =lambda n:fact(n)
    print(factorial(n))
'''

#EX.
'''
Max=lambda seq : max(seq)
print(Max([5,9,1,6]))
'''



################# LAMBDA FUNCTIONS #######################





########THERE ARE THREE TYPE OF LAMBDA FUNCTIONS
####(A). Filter
####(B). Map
####(C). Reduce
###


########(A).Filter
#basics syntax EX.
'''
filter (fun,seq)
filter (doubler,[2,4,6,8])
'''

# Genral syntax



#EX. """"wrong"""
'''
#n=int(input("N;"))
def dou(n):
    return n*2
print(filter(dou,[5,4,8,1,2,7]))
'''




#EX. find the even numbers by using filter function from"LAMBDA FUNCTION".
'''
def even(n):
    if n%2==0:
        return True
    return False
print(list(filter(even,[5,4,8,1,2,7])))  #[4,8,2]
'''


#EX. take age of users and solve it if the age is less than 18 it is not our accpeted user:

'''
def ismajor(age):
    if age>=18:
        return True
    return False
ages=[21,18,19,25,26,27,16,15,59,56]
majors=list(filter(ismajor,ages))
print(majors)
'''



#EX. take age of users and solve it if the age is less than 18 it is not our accpeted user same but some ages is negative;
'''
def ismajor(age):
    if age>=18:
        return True
    return False
ages=[21,18,19,25,26,-27,16,-15,59,56]
majors=list(filter(ismajor,ages))
print(majors)
'''



#Ex. take age of users and solve it if the age is less than 18 it is not our accpeted user:
'''
ages=[24,20,18,14,15,10,19,20]
majors=list(filter(lambda age:age>=18, ages))
print(majors)
'''


#EX. write a program that print all the list that is in non zero elements and also print the max out puts of the lists.
'''
ages=[[21,18,19],[24,20,18],[0,15,10],[19,20,12]]
allseq=list(filter(all,ages)) #all is automatically erase the list which is in zero. 
maxseq=list(filter(max,ages)) #max is automatically take all the lists.
print(allseq)
print(maxseq)
'''




########################################### Map #############################################################################
#####################################################################################################################
####### 


#base syntax:
'''
map (fun,seq)
map(upper(),"niet")
'''

#General syntax;


#EX.
#   ####OUTPUT:-        ['N', 'I', 'E', 'T']

'''
seq="niet"
res= map(lambda ch : ch.upper(),seq)
print(list(res))
'''
#   """"WRONG""""
'''
seq="niet"
res= map(lambda ch : ch.upper(),seq)
print(list(''r.join(res))
'''
#
#   #####OUTPUT:-       NIET
'''
seq="niet"
print(seq.upper())
'''



#EX.
'''
seq=['2','5','9','12','45',]
res=list(map(int,seq))
print(res)
'''

#EX. write a program for f(x)=ax**2+bx+c.
'''
x=[1,2,5,0.5,3]

def transform(x):
    a,b,c=10,2,5
    return a*x*x+b*x+c
seq=list(map(transform,x))
print(seq)
'''



#EX.same output but somethings diffrenet
'''
def tra(x):
    a,b,c=10,5,2
    return (a*x*x)+(b*x)+c
xseq=[1,2,4,5,3,0.5,2.5]
trans=list(map(tra,xseq))
print(trans)
'''



#EX.
'''
seq=[1,2,3,4,5,6]
sqr=list(map(lambda x:x**2,seq))
print("Our List is:",seq)
print("The square of the list is:",sqr)
'''


#EX.

#######################################################################################
########################################################################################
#########################################################################################
#########################################################################################






################################## Reduce #########################################
##################################################################################
#########in REDUCE function


# Base Syntax:
'''
seq=[1,4,7,8,6]
reduce (fun,seq)
reduce(lambda a,b:a+b,seq)
'''



#EX.write a program to add all the elements of the list:
'''
from functools import reduce
seq=[1,4,7,8,6]
sum=reduce(lambda a,b:a+b,seq)
print(sum)
'''


#EX. same
#### """WRONG"""
'''
from functools import reduce
seq=[1,4,7,8,6]
Max=list(reduce(lambda a,b: seq))
print(Max)
#maxseq=list(filter(max,ages)) #max is automatically take all the lists.
'''



#EX.    find the greatest number in the list:
'''
from functools import reduce

ages=[20,22,26,29,55,100,108,99,36,5]
Max=reduce(lambda a,b:a if a>b else b, ages)
print(Max)
'''


#EX.user defined function  find the greatest number in the list:

'''
ages=[20,22,26,29,55,100,108,99,36,5]

from functools import reduce

def maximum(a,b):
    if a>b:
        return a
    return b
Max=reduce(maximum,ages)
print(Max)
'''



#EX.
'''
ages=[12,15,14,18,20,45,70]
from functools import reduce
def maxm(a,b):
    if a>b:
        return a
    return b
maxma=reduce(lambda a,b



             '''




################################### MODULES ################################################

#######################
#It is the collection of all the functions
#We can import the pre define module in our program with following ways:

#(1). from moduleName import *   ### This statement imports all the modules that is defined. 
#(2). from moduleName import fun1 ---> ##fun1 is only the name of one function
#(3). from moduleNameimport fun1,fun2,sun3...,fun n ------> ##this use to import multiple functions.
#(4). import moduleName as shortName ----> this use to set one module one name (as---> Alias)
#(5). from moduleName import lenthyfunName as shortName ----> we can as a function also.
#


#############################BUILT IN MODULES #######################################################

#Ex. import all the math functions by using this.
'''
from math import *
print(dir())
'''


#EX.

'''
from math import *
'''
'''
print(factorial(6))
print(pow(8,3))
print(sqrt(25))
print(gcd(8,2)) #gcd ----> HCF
#print HCF for any numbers
print(gcd(8,2,3,5,5,6,4,68,4))
'''
'''
from math import sqrt
print(sqrt(25))
#but you are not install factorial function so factorial gave you error
print(factorial(6))
'''
'''
from math import sqrt,factorial
print(sqrt(25))
print(factorial(6))
'''




#EX. use of ASLIS function:
'''
import math as m
print(m.sqrt(25))
print(m.pow(8,2))
'''

#EX. Use another example for use ASLIS function:
'''
import math as m
import functools as ft
print(ft.reduce(lambda a,b:a+b,[2,4,5]))
'''
'''
from math import factorial as fact
print(fact(45))
#"""WRONG"""
#print(math.fact(45))
'''
'''
from math import factorial as fact
print(fact(4))
'''



###################################### USER DEFIND MODULES #####################################

########### Some modules defind by the user.
#################User-defined python modules are the modules, which are created by the user to simplify their project. These modules can contain functions, classes, variables, and other code that you can reuse across multiple scripts.
##########

#EX.
#in my system i have save the calculator file with the name of "calc.py" and i can excucate the program in the new file name "new calc.py" and write "from calc import *" to import all the function into the "new calc.py" file.


#EX.
