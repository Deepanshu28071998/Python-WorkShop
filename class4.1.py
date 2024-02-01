###########################FUNCTION####################
#############Function is block of statements excecutes on its call.Functions can be use to writen by processing inputs.
#####(1).   PRE-DEFINED FUNCTIONS
#####(2).   USER-DEFINED FUNCTION
#(1). PRE-DEFINED FUNCTIONS
'''
#int--> reads input from user 

#Print--->

#len()--->

#max()--->

#min()--->

#pow()--> calculates power of two numbers
        #


'''

###Execute all functions:-
#print(pow(5,2))
#print(len())


'''
import math
print(dir())
'''
'''
from math import *
print(dir())
'''
'''
from math import *
from os import *
print(dir())
'''


#####(2). USER-DEFINED FUNCTIONS:-
#####USER-DEFINED FUNCTIONS are written by the user/programmer at the time of writing the application.
####    It has 'FOUR' types:
#### (a). def funcName(args):
####            Statement1
####            Statement2
####            return expr             (Writen statements)
####     funcName(args)

'''
###
def product(a,b):
    res=a*b
    return res
###
'''

#EX.
'''
def product(a,b):
    res=a*b
    return res
print(product(5,4))
'''

#EX.
'''
def div(a,b):
    que=a/b
    rem=a%b
    return(que,rem)
print(div(9,2))
'''
#EX. EVEN or ODD
'''#self try
def evenorodd(x):
    if(x%2==0):
        print("EVEN")
    else:
        print("ODD")
    return (x)
print(evenorodd(25))
'''

#####EX. division
'''
def div(a,b):
    q=a//b
    r=a%b
    return q,r
n=int(input("Enter Numerator: "))
d=int(input("Enter denominator: "))
qu,re = div(n,d)
print("Quotient: ",qu)
print("Reminder: ",re)
'''


###Crete it with while true condition (self try):
'''
while True:
    print("\n")
    def div(a,b):
        q=a//b
        r=a%b
        return q,r
    n=int(input("Enter Numerator: "))
    d=int(input("Enter denominator: "))
    qu,re = div(n,d)
    print("Quotient: ",qu)
    print("Reminder: ",re)
'''



#########TYPES OF USER DEFINED FUNCTIONS########
#####(1). with return and with arguments ---> It is most used function.
#####(2). with return and without arguments ---> 
#####(3). without return and with arguments --->
############(4). without return and without arguments :-
####
####
#EX.
'''
def add(a,b):
    res=a+b
    print(res)
add(5,4)
'''


######(1). with return and with arguments :-
###
#EX.
'''
def add(a,b,c):
    return a+b+c
sum=add(5,2,8)
print(sum)
'''

###(2). with return and without arguments
######
#EX.
'''
def add():
    a=int(input("Enter the value: "))
    b=int(input("Enter the value: "))
    c=int(input("Enter the value: "))
    return a+b+c
sum=add()
print(sum)
'''



#######(3). without return and with arguments :-
####
####
#EX.
'''
def add(a,b):                          ####None
    res=a+b                            ###None
    print(res)                         ###None
add(5,4)
'''
### defualt return type of any user defined function is "None".


#######(4). without return and without arguments :-
####
####
#EX.
'''
def add():
    a,b=5,4
    res=a+b
    print(res)
add()
'''




###################TYPE OF ARGUMENTS###################
###(1). POSITIONAL ARGUMENTS
###(2). DEFAULT ARG.
###(3). KEYWORD ARG.
###(4). ARBITRARY ARG.
    ###(a). variable length keywords arg.
    ###(b). variable length non-keywords arg.


######(1). POSITIONAL ARGUMENTS:-
#####
#EX.
'''
def add(a,b,c):
    print(a,b,c)
    res =a+b+c
    return res
add(4,8,3)
'''
#Ex. change position:
'''
def add(a,b,c):
    print(a,c,b)
    res =a+b+c
    return res
add(4,8,3)
'''
#EX. Function call multiple time:
'''
def add(a,b,c):
    print("a=",a,"b=",b,"c=",c)
    res =a+b+c
    return res
sum=add()
print(sum)
add(4,8,3)
add(9,5,4)
'''

#EX. write the name:-
'''
def fullName(first,last):
    return(first+" "+last)
print(fullName("Deepanshu","Jain"))
'''
#EX. write name last+first:-
'''
def fullName(first,last):
    return(last+" "+first)
print(fullName("Deepanshu","Jain"))
'''

#####(2). DEFAULT ARG. :-
####
#EX.
'''
def add(a,b,c):
    print(a,b,c)
    res=a+b+c
    return res
add(4,8,3)
'''

#EX.
'''
def add(a,b,c=0):
    print(a,b,c)
    res=a+b+c
    return res
add(4,8,3)
add(5,4)
'''

#EX.
'''
def add(a,b=0,c=0):
    print(a,b,c)
    res=a+b+c
    return res
add(4,8,3)
add(5,4)
add(8)
'''
#EX.
'''
def add(a=0,b=0,c=0):
    print(a,b,c)
    res=a+b+c
    return res
add(4,8,3)
add(5,4)
add(8)
add()
'''

#EX.


#EX.
'''
def product(a=1,b=1,c=1):
    print(a,b,c)
    res=a*b*c
    return res
print(product(4,8,3))
print(product(5,4))
print(product(0,4))
print(product(8,5,0))
print(product())
'''

#Ex.
'''
def product(a=1,b=1,c=1):
    print(a,b,c)
    res=a*b*c
    return res
print(product(a=4,b=8,c=3))
'''






#EX. change the position
'''
def product(a=1,b=1,c=1):
    print(a,b,c)
    res=a*b*c
    return res
print(product(b=4,a=8,c=3))
'''


#####(3). KEYWORD ARG.:- It pass arg. with their name.
###
#EX.
'''
def fullName(last,first):
    return(first+" "+last)
print(fullName(first="Deepanshu",last="Jain"))
'''
#EX.
'''
def fullName(last,first):
    return(first+" "+last)
print(fullName(first="Deepanshu",last="Jain"))
print(fullName(last="Jain",first="Deepanshu"))
'''
#EX.





#####ARBITRARY ARG.
    ###(a). variable length keywords arg.
    ###(b). variable length non-keywords arg.
###
#####(a). variable length keywords arg.:-
###
#EX.
#wrong
'''
def product(**args):
    print(args.items())
    for k,v in args.items():
        print(k,v)
product(a=5,b=7,c=9,d=3,e=2)
'''

#EX.
'''
def product(**args):
    res=1
    for k,v in args.items():
        res*=v
    return res
print(product(a=5,b=7,c=9,d=3,e=2))
'''





######(b). variable length non-keywords arg. :-
###

#EX.
'''
def product(*values):
    print(values)
    print(type(values))
    res=1
    for e in values:
        res*=e
    return res
    

print("\n",product(6,7,4,5,9,1))
print("\n",product(6,7,4,5))
'''
#EX.
'''
def product(*values):
    print(values)
    print(type(values))
    res=1
    for e in values:
        print(e,end=' ')
        res*=e
    return res
    

print("\n",product(6,7,4,5,9,1))
print("\n",product(6,7,4,5))
'''

#EX.
'''
def product(*values):
    #print(values)
    #print(type(values))
    res=1
    for e in values:
        #print(e,end=' ')
        res*=e
    return res
    

print("\n",product(6,7,4,5,9,1))
print("\n",product(6,7,))
print("\n",product(6,7,4,5,8,4,5,9,1))
#print("\n",product(6,7,4,5))
'''

#EX.
###Wrong
'''
def product(**args):
    print(args.item())
    for k,v in args.item():
        print(k,v)

product(a=5,b=7,c=9,d=3,e=2)


#print("\n",product(6,7,))
#print("\n",product(6,7,4,5,8,4,5,9,1))
#print("\n",product(6,7,4,5'''


#######################################################################
#######################################################################
#######################################################################

#SCOPE OF VARIABLES :-
#VARIABLES ARE TWO TYPES:-
#(1). LOCAL VARIABLE
#(2). GLOBAL VARIABLE


####(1). LOCAL VARIABLE:- variables which are define in side a block/Function. changes into this will not caried out side the block.
####
###

#ex.
'''
def modify(n):
    n+=5
    print("inside fun: ",n)
n=20
print("before modify: ",n)
modify(n)
print("after modify: ",n)
'''
#####SCOPE OF LOACAL VARIABLE Is with in the block:
#ex.
#Error
'''
def modify(n):
    a=5
    n+=a
    print("inside fun: ",n)
n=20
print(a)
print("before modify: ",n)
modify(n)
print("after modify: ",n)
'''
#ex.
'''
def modify(n):
    a=5
    n+=a
    print("inside fun: ",n)
n=20
print("before modify: ",n)
modify(n)
print("after modify: ",n)
print(a)
'''


#ex.
'''
def modify(n):
    n+=5
    print("inside fun: ",n)
n=20
print("before modify: ",n)
modify(n)
print("after modify: ",n)

'''



#(2). GLOBAL VARIABLE :- varibles which can be access throug out the program. at any point of line SCOPE will be completed.


#EX.
'''
a=50 #a is local var.
def modify(n):
    n+=a
    print("inside modify():",n)
def multiply(n):
    n*=a
    print("inside multiply:",n)
n=20 #n is global var.
print("before modify:",n)
modify(n)
print("after modify:",n)
print(a)
multiply(n)
print("after multiply:",n)
'''


#EX. we can not change the valueof loval var. in excecution time.
#
'''Traceback (most recent call last):
  File "E:/Python workshop/class4.1.py", line 541, in <module>
    modify(n)
  File "E:/Python workshop/class4.1.py", line 532, in modify
    n+=a
UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
'''
'''
a=50 #a is local var. #cannot access local variable 'a' where it is not associated with a value.
def modify(n):
    n+=a
    print("inside modify():",n)
    a=1
    a=100
def multiply(n):
    n*=a
    print("inside multiply:",n)
n=20 #n is global var.
print("before modify:",n)
modify(n)
print("after modify:",n)
print(a)
multiply(n)
print("after multiply:",n)
'''
#EX. Another type of process:
'''
a=50 #a is local var.
def modify(n):
    a=1
    n+=a
    print("inside modify():",n)
    a+=100
def multiply(n):
    n*=a
    print("inside multiply:",n)
n=20 #n is global var.
print("before modify:",n)
modify(n)
print("after modify:",n)
print(a)
multiply(n)
print("after multiply:",n)
'''


######################################################PART2#####################################################################################################################################################################
#########################################################################################
#############################################################################################
########################################################
###############################
##################
###########
########
####
#
#
##
#
#
#

#
#
#

#
#
#************************************************************************************************
