'''
print(3+(2+3j))
print(2+3)
print(2.5+3)
print(4.5+7.5)
print(4+(5+6j))
print('a'+'b')
print((5+6j)+4)
print(5+6j+4)
#print(5.5+'A')
#print(4+6j+'A')
print('A'+'B')
print("A"+"B")
#print(''''ABC''''+''''DEF'''')
print(4+7j+5-8j)
a= 7.5
b=complex(a)
print(a,b)
##Subtraction opration
print(4-7)
print(7.5-1.5)
print(3.0-5.)
print(7-(6+8j))
print(5.5-6-8j)
#print("ABC"-"A")
'''
##multiplication operation
'''
print(4*5)
print(10*2.5)
print(2.5*3.0)
print(2.5*2.5)
print('a'*4)
print('a'*2)
'''
##Division operator
'''
print(8/2)
print(10/2.0)
print(10.0/2.0)
print(10/2.0)
print(15/2)
print(15/2.5)
'''
#mingal division
'''
print(10//2)
print(123//4)
print(123//10)
print(57//10)
print(10045//10)

print(14.5//2)
print(75.5//2.0)
#print('A'//2)
#print((4+2j)//2+j)
print((4+2j)/2)
#print((4//2)+(2//2)'j')
'''

##Modulo operator
'''
print(10%2)
print(14%3)
print(5%4)
print(4%5)
#print('A'%2)
'''


'''
print(3+4-2)
print(3*4-2+4-5)
'''

#'''PEMDAS rule is follow in these cases
#powres
'''
print(4**8)
print(4.5**2)
#print('A'**2)
'''



#########Relational operators############
'''
a=8
b=9
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
'''

###ASCII Values on relation operators:-
'''
print('a'<'b')
print('a'=='b')
print('a'=='b')
'''
'''
print('a'>'A')
print('b'<'a')
'''
'''
print('a'<='A')
print('abc'=="abc")
print("abc">"abc")
print("abd"<"abc")
print("abd">"abc")
print("abd"<="abc")
print("abd">="abc")
print('abc'>'ab')
'''
'''
print(" ">'')
'''




######Logical Operators:-
'''
###print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(False and 12)
print(12 and 10 and 89)
print(12 and 10 and 89 and 'a')
print(12 and 10 and 0 and 'a')
print(12 and 10 and 1 and 'a')
print(12 and 10 and False and 'a')
'''
'''
print(12 and 10 and 0 and False and 89)
print(12 and 10 and False and 0 and 89)
print(5<6 and 6<8)
'''
'''
print(-67 and 54 and 'abc')
print(0 and 54 and 'abc')
'''
###print("OR")
'''
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(False or False or False or False or False or False)
print(False or False or False or False or False or True)
'''
'''
print(12 or 15 or 54)
print(0 or 0 or 0)
print(0 or 15 or 54)
print(45 or 0 or True)
print("niet" or "noida" or "mca")
print(False or 0 or False or True)
print(False or 0 or False or True or 123 or 459)
###print("NOT")
'''
'''
'''
'''
'''
'''
print(not True and  True)

print(not True and  False)
print(False not True)
print(False not False)
'''
'''
print(not True and True)
print(not True and  True)
print(not 0 and 1)
print(not "abc" and "abc")
'''
'''
print(not "False")
print(not -1)
print(45 and 24 or 12)
print(45 or 24 and 12)
print(45 and 45 or True and 100)
print(not 24 and -4 or 5 and not True)
print(not 24 and -4)
print(5 and False)
print(5 and not True)
print(False and False)
'''




########ASSIGNMENT OPERATORS:-###########
'''
a=4
a+=2
#a=a+2=6
print(a)
a-=3
#a=a-3=6-3=3
print(a)
a*=4
#a=a*4=3*4=12
print(a)
a**=2
#a=a**2=12**2=144
print(a)
a/=2
#a=a/2=144/2=72.0
print(a)
a//=4
#a=a//4=72//4=18.0
print(a)
'''



#########BITWISE OPERATORS#########
#####BITWISE AND
'''
print(4&2)
print(3&7)
print(7&1)
print(6&1)
print(9&1)
print(13&1)
print(16&1)
print(24&1)
'''

'''
print(123%10)
print(456%10)
print(1004%10)
print(1458%1000)
'''
######BITWISE OR
'''
print(3|4)
print(4|8)
print(1|3)
print(1|5)
print(1|2)
'''
#######BITWISE EXCLUSIVE OR
'''
print(1^1)
print(1^0)
print(0^1)
print(0^0)
'''
'''
print(5^4)
print(12^12)
print(7^6)
print(6^7)
'''
#FORMULA:-       print('n'^'n-1')
#########TILTE OPERATER##########
#FORMULA:-      ~x=-(x+1)
'''
print(~1)
print(~-1)
print(~6)
print(~-6)
'''

######SHIFTLEFT << #######
'''
print(8<<1)#16 
print(8<<2)#32
print(8<<3)#64
print(8<<4)#128
'''
'''
print(3<<1)#6 (110-->6)
print(3<<2)
print(3<<3)
print(3<<4)
print(124<<2)
####FORMULA RULE:- N*2**n
'''
#print(4.5<<1)


#######SHIFT RIGHT >> #######
'''
print(16>>1)
print(16>>2)
'''



#######MEMBERSHIP OPERATOR########
'''
print('a' in "niet")
print('i' in 'niet')
print('ni' in 'niet')
print('Ni' in 'niet')
#print(123 in '1234')
#print(123 in 1234)
print('123' in '1234')

print(1 in [1,2,3])
print('1' in [1,2,3])
'''
##########IDENTITY OPERATORS##########
'''
print(10 is 10)
print(0 is not 5)
print('a' is not 'A')
print(0 is 5)
'''
'''
a=10
b=10
print(a is b)
print(a is not b)   ######ID#####
print(id(a))
print(id(b))##"The ID of a is same the ID of b because both store the same value so there addersses are also same" "
'''
'''
a='a'
b='b'
print(a is 'a')
'''


'''
print("Hello")
a =10
a=16
b=20
c=a+b
print(c)
print('NIET')
'''
#########CONDITIONAL STYTEMENTS#########
#(1). if
'''
a=int(input("Put a intiger number: "))
if a>10:
    print(a," is Greater then 10")
print("Thank you")
'''
#ex. 2
'''
num = int(input("Enter a number: "))
if (num>0):
    print("'I' m a positive number")
    print("I'm inside if block")
print("I'm outside if block")
print("End of the program")
'''

#(2). if-else
'''
a=int(input("Put a intiger number: "))
if a>10:
    print(a," is Greater then 10")
else:
    print(a," is Less then 10")
print("Thank you")
'''
#ex. 2
'''
num = int(input("Enter a number: "))
if (num>0):
    print("'I' m a positive number")
    print("I'm inside if block")
else:
    print("I'm outside if block")
    print("End of the program")
'''

#(3). if-elif-else
'''
a=int(input("Put a intiger number: "))
if a>=10:
    print(a," is Greater then 10")
elif a>=5:
    print(a," is Less then 10 but Greater then 5")
else:
    print(a," is Less then 10 and 5 both.")
print("Thank you")
'''
#ex.2
'''
num = int(input("Enter a number: "))
if (num>0):
    print("'I' m a positive number")
    print("I'm inside if block")
elif (num<0):
    print("'I' m a Negetive number")
    print("I'm inside elif block")
else:
    print("I'm Zero")
    print("I'm outside if block")
print("End of the program")
'''





#if-elif-elif-else
###using 'AND'
'''
age = int(input("Enter your age: "))
if age<18:
    print("You can't vote.")
elif age>=18 and age<20:
    print("You can Vote.")
elif age>=20 and age<25:
    print("You can vote and eligible for participating on M.A.L. elections")
elif age>=25 and age<30:
    print("You can vote and eligible for participating on M.P. elections")
else:
    print("You can vote and eligible for C.M. and P.M. posts.")
'''
#ex2.
'''
age=int(input("Enter your age"))
if age>=10 and age<18:
    print("Cycle chalao")
elif age>=18 and age<20:
    print("Bike mang mat lio")
elif age>=20 and age<25:
    print("Chal ab Bike chla le")
elif age>=25 and age<60:
    print("Car bhi chla lo ab to.")
else:
    print("Buddha hogya h chupchap mandir ja kya bike or car ke piche lga h.")
'''
#Sir do these programes:-
'''
num= int(input("Enter a number: "))
if (num%2==0):
    num+=20
elif (num%3==0):
    num+=30
elif (num%5==0):
    num+=50
elif (num%7==0):
    num+=70
else:
    print("I'm zero")
print("num",num)
print("End of the program")
'''
'''
num= int(input("Enter a number: "))
if (num%2==0):
    if (num%3==0):
        num+=30
    else:
        num+=10
else:
    if (num%5==0):
        num+=50
    else:
        num+=20


print("num",num)
print("End of the program")
'''



####Another Method for write if statement
'''
a=20
b=3
if a>b: print(a," is greater than",b)
'''
######H.W.#######
'''
a = int(input("Enter the number: "))
if (a%3==0):
    if (a%7==0):
        print("Our Fav.")
    else:
        print("Sir Fav.")
elif (a%7==0):
    print("My fav.")
else:
    print("Not Fav.")
'''




###Prog1.1:-(by sir)
'''
bal= 1000
print("1. Deposit \n2. Withdraw \n3. Balance Enquiry")
ops=int(input())
if(ops==1):
    amount=int(input("Enter amount to deposit: "))
    bal+=amount
    print("Transaction completed sucessfully...")
    print("Available balance: ", bal)
elif (ops==2):
    amount=int(input("Enter the amount to be withdrawn:"))
    if (amount<=bal):
        bal-=amount
    else:
        print("Insufficient funds in your account.")
    print("Transaction completed successfully.")
    print("Available balance: ", bal)
elif (ops==3):
    print("Available balance: ",bal)
else:
    print("Invalid operation")
    
'''
######CIRCULER LINKED LIST (with SOME error)#####

'''
while True:
    bal= 1000
    print("\n\n\n\n1. Deposit \n2. Withdraw \n3. Balance Enquiry \n4. EXIT")
    ops=int(input())

    #ops=int(input())
    if(ops==1):
        amount=int(input("Enter amount to deposit: "))
        bal+=amount
        print("Transaction completed sucessfully...")
        print("Available balance: ", bal)
    elif (ops==2):
        amount=int(input("Enter the amount to be withdrawn:"))
        if (amount<=bal):
            bal-=amount
        else:
            print("Insufficient funds in your account.")
        print("Transaction completed successfully.")
        print("Available balance: ", bal)
    elif (ops==3):
        print("Available balance: ",bal)
    elif (ops==4):
        break
    else:
        print("Invalid operation")
    
'''





















#####################################################################
#####################################################################
'''
a=0
b=1
c=a+b
n=int(input('Enter the value: '))
if (n==1):
    print(a,b,c)
else:
    print(a,b,end=' ')
    while(c<=n):
        print(c,end=' ')
        a=b
        b=c
        c=a+b
'''



####################H.W. #############Ass.
'''
a=0
b=1
c=a+b
n=int(input('Enter the value: '))
if (n==1):
    print(a,b,c)
else:
    print(a,b,end=' ')
    while(c==n):
        print(c,end=' ')
        a=b
        b=c
        c=a+b
'''
