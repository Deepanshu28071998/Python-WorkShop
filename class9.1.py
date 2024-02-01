###############  STRING    ####################
# STRING is a seq.of characters. Which can be repaeted with singh Quotes ' ' , Dobule Quotes " " , Tripal Quote ''' '''

#EX.
'''
s1='A'
s2="A"
'''
#s3='''A'''             #CORRECT
'''
print(s1)
print(type(s1))
print(s2)
print(type(s2))
print(s3)
print(type(s3))
print(id(s1))
print(id(s2))
print(id(s3))           #The adress of all three will be same because the value of the string is same....
'''


'''
n1=159
s1=str(n1)
print(n1,type(n1))
print(s1,type(s1))

#OUTPUT---->
#159 <class 'int'>
#159 <class 'str'>
'''
'''
c=chr(65)
print(c)
print(type(c))

#OUTPUT--->
#A
#<class 'str'>
'''
'''
c2="M"
print(ord(c2))
print(type(c2))
#OUTPUT--->
#77
#<class 'str'>
'''


'''
s='python'

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
#ERROR  print(s[6]) ## IndexError: string index out of range
'''

'''
s2="NIET MCA"
print(s2[2])
print(s2[4])
print(s2[-1])
print(s2[-3])
print(s2[-5])
print(s2[-6])
print(s2)
print(s2[0])
print(s2[1])
print(s2[2])
print(s2[3])
print(s2[4])
print(s2[5])
print(s2[6])
print(s2[7])
'''
#ERROR:-        #because it is out of range #IndexError: string index out of range
'''
print(s2[8])
print(s2[9])
print(s2[10])
print(s2[11])
print(s2[-9])
'''

'''
s3="NIET MCA"
#ERROR     s3[-2]='B'          #The single letter can't be change in the string
print(s3)
s3="NIET MBA"
print(s3)                   # we can change the whole string.
'''
#We erase the entier string and write a newstring on the "s3" variable....



######DEL()####
#WE use DEL function to delete whole string in the variable....
'''
s3="NIET MCA"
print(s3)
del(s3)
print(s3)
#  NameError: name 's3' is not defined
#It gave use NameError.
'''

'''
import string
print(string.ascii_letters)
#OUTPUT--->     abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
#OUTPUT---->        abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)
#OUTPUT--->     ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.punctuation)
#OUTPUT--->     !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.digits)
#OUTPUT--->     0123456789
print(string.octdigits)
#OUTPUT---->    01234567
print(string.hexdigits)
#OUTPUT---->   0123456789abcdefABCDEF0123456789abcdefABCDEF
'''





###EX.
'''
s1="Ashutosh"
print(s1.startswith("A"))           # In this case It gave us True if the condition start with the giving letter. otherwise it gave us False...
print(s1.startswith("Ash"))
print(s1.startswith("ash"))         # It gave False because Python is a case sensitive langauge....   
print(s1.startswith("Ashutosh"))
'''

'''
s2="Dharmesh"
print(s2.endswith('h'))     #True       # In this case it end with the same string it gave True otherwise it gave us False...
print(s2.endswith('H')) #False
print(s2.endswith('ramesh')) #false
print(s2.endswith('harmesh')) #True
print(s2.endswith('Dharmesh')) #True
'''

'''
s3="We are Masters."
r=s3.replace('e','o')
print(s3)
print(r)
#we replace 'e' to the 'o' in s3 strintg. but we cann't change s3 string we store in new variable....  
#Output-->
#We are Masters.
#Wo aro Mastors.

nr=s3.replace('are','became')
print(nr)
#we replace 'are' to the 'became' in s3 strintg. but we cann't change s3 string we store in new variable....  
rr=s3.replace('We are Masters.','I am Master.')
print(rr)
print(s3)
'''

###ISDIGIT#####
'''
s="15923"
print(s.isdigit()) #True      #if digits in it it gave us True... otherwise it gave us False....
a="12345a"
print(a.isdigit()) #False   #because init 'a' is. so it is not digit...
b="15923&"
print(b.isdigit())  #False  #because '&' is a spacial symbol...
c="153.45"
print(c.isdigit())  #False  #because "." (decimal sing) is a spacial symbole so it gave False... 

a="124 52"
print(a.isdigit())  #false #because " "(space) is a spacial character....
'''

###### ISAPLHA() ######
'''
s="nietnoida"       #true
print(s.isalpha())
s2="niet-noida"     #False
print(s2.isalpha())
s3="niet noida"     #false
print(s3.isalpha())
s4="niet9noida"     #false
print(s4.isalpha())
s5="NietNoida"      #false
print(s5.isalpha())
'''
######## isdecimal() #########

'''
s='15964'
print(s.isdecimal())        #True #because all values are digits... The entier number is single value...
a='156.49'
print(a.isdecimal())        #False #because in this '.' (dot) is a spaceial character....
'''


###### ISNUMERIC()  #############
'''
s="159745"
print(s.isnumeric())            #True 
s2='1544.44'
print(s2.isnumeric())               #False
s3='1544abc'
print(s3.isnumeric())           #False
'''


########  ISALNUM()  ############
'''
s="159745"
print(s.isalnum())            #True 
s2='1544.44'
print(s2.isalnum())               #False
s3='1544abc'
print(s3.isalnum())           #True  #because string is considar as numeric in this case
s4='abc'
print(s4.isalnum())             #true #because string is considar as numeric in this case
s5='mv@64'
print(s5.isalnum())             #False #for spacial symbol
'''


##### isupper() AND islower()  #######

'''
a="A"
print(a.isupper())      #True

s="a"
print(s.isupper())      #False


print(a.islower())          #False
print(s.islower())          #True
'''
'''
b="A2"
print(b.isupper())      #True #because A and 2 both is upper case letters....
print(b.islower())      #False #because A is not a lower case letters....


c="a2"
print(c.isupper())      #False #because 'a' is not a upper case letters....
print(c.islower())      #True #because 'a'  is lower case letters....


d='A2b'
print(d.isupper())      #False #because 'a' is not a upper case letters....
print(d.islower())      #False #because 'A'  is not a lower case letters....
'''


########### istitle()  ###########
'''
s="Tit For Tat"
print(s.istitle())#True #because it is capitalize


s2="Tit for tat"
print(s2.istitle()) #False
'''


######## Excecution of upper, lower, title, capitalize, swapcase ########
'''
s="NIET"
print(s.upper())
print(s.lower())
print(s.title())
'''

'''
s="NiEt is oUr EmoTion"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
'''
#OUTPUT--->
'''
NIET IS OUR EMOTION
niet is our emotion
Niet Is Our Emotion
Niet is our emotion
nIeT IS OuR eMOtION
'''







###if it check True or False condition we use 'is'---> .isdigit,
###
###
###
###
##############################################################
###################### PART 2 #########################


############### partition ###############

'''
s="We like Python Programming"
print(s.partition (" "))    # output---> ('We', ' ', 'like Python Programming')

print(s.partition("like"))  #output---> ('We ', 'like', ' Python Programming')

print(s.partition("was"))   #output---> ('We like Python Programming', '', '')

print(s.partition("We"))    #output--->  ('', 'We', ' like Python Programming')
'''
#================================
######## INDEX() ########

'''
s="We like Python Programming"
print(s.index('P'))         #the first 'P' is in 8th position so it gave 8....
print(s.index('g'))
#ERROR     print(s.index('z'))     #ValueError: substring not found  
print(s.index('like'))      #position of 'like' is 3....
#ERROR     print(s.index("program"))   #ValueError: substring not found
#in it 'p' of program is small p not capital 'P'...   
print(s.index("Python"))
'''
#### find() ######
#find is like INDEX function but if the letter of value not present in the variable it gave -1.....
#
'''
s="We like Python Programming"
print(s.find('P'))         #the first 'P' is in 8th position so it gave 8....
print(s.find('g'))
print(s.find('z'))     #gave -1  
print(s.find('like'))      #position of 'like' is 3....
print(s.find("program"))   #Gave the -1 value  
print(s.find("Python"))
'''



########### rindex() ###########
#rindex() from right side 
'''
s="We like Python Programming"
print(s.rindex('P'))         ##the first 'P' from 'RIGHT side' is in 15th position so it gave 15....
print(s.rindex('g'))
#ERROR     print(s.rindex('z'))     #ValueError: substring not found  
print(s.rindex('like'))      #position of 'like' is 3....
#ERROR      print(s.rindex("program"))   #ValueError: substring not found
#in it 'p' of program is small p not capital 'P'...   
print(s.rindex("Python"))
'''


##### rfind #####

'''
s="We like Python Programming"
print(s.rfind('P'))         #the first 'P' from 'RIGHT side' is in 15th position so it gave 15....
print(s.rfind('g'))

print(s.rfind('z'))     #-1  
print(s.rfind('like'))      #position of 'like' is 3....

print(s.rfind("program"))   #-1
   
print(s.rfind("Python"))
'''
#==========================================


############    SPRIT LINES ##########################
'''
s="We like Python Programming.\nWe are awesome.\n We are Masters"
print(s.splitlines())
#It splits the lines....
#OUTPUT--->   ['We like Python Programming.', 'We are awesome.', ' We are Masters']
'''



##########    Count()      ##########################
'''
s="We like Python Programming.We are awesome.We are Masters"
print(s.count('W'))     #count 3 times
print(s.count('We'))
print(s.count('Python'))
print(s.count('e'))
print(s.count(''))      #count no. of letters in the string.... 57
print(s.count(' '))     
print(s.count('.'))
'''


################ max,min,len,any,all   ##############

'''
s='Python'
print(len(s))
print(max(s))           #gave 'y' as maximum by using their ASCII values.
print(min(s))           #gave 'y' as minimum by using their ASCII values.
print(any(s))           #true   because in s any non zero element is not present.
print(all(s))           #true   because in s all elements are non zero.
#ERROR   print(sum(s))  #TypeError

print(any(""))          #False  because any gave us 
print(all(""))          #True   because all gave us 
'''


#################    slicing #####################

s="Engineering"
'''
print(s[:])
print(s[:6])
print(s[3:])
print(s[2:9])
print(s[::-1])
'''
#OUTPUT---->
'''
Engineering
Engine
ineering
gineeri
gnireenignE
'''
'''
print(s[-2:-8:-1])
print(s[8:1:-1])
'''
#OUTPUT---->
'''
nireen
ireenig
'''

#########################################################
#IMP. Q.
#len(string)>=7 and odd
#And print the middle three letters....

'''
def getm3(s):
    mid=len(s)//2
    res=s[mid-1]+s[mid]+s[mid+1]
    return res

s=input("String: ")
print(getm3(s))

#Another method:-

def get(s):
    mid=len(s)//2
    res=[s[mid-1:mid+1+1]]
    return res
s=input("String: ")
print(get(s))
'''


#IMP. Q.
#len(string)>=7 and odd
#k<=len(string) and odd
'''
def getm3(s):
    mid=len(s)//2
    res=s[mid-(k//2):mid+(k//2)+1]
    return res

s=input("String: ")
k=int(input("Enter the middle values you want: "))
print(getm3(s))
'''
#IMP. Q.
#len(string)>=7 and odd
#k<=len(string) and odd

#condition:
#len(string)<7--> Invalid string
#k>len(strin)---> Not possible
####
    
'''
def getm3(s,k):
    if(len(s)<7):
        return "Invalid String"
    if (k>len(s)):
        return "Not possible"
    mid=len(s)//2
    res=s[mid-(k//2):mid+(k//2)+1]
    return res

s=input("String: ")
k=int(input("Enter the middle values you want: "))
print(getm3(s,k))
'''
###In while loop
#ERROR
'''
n=int(input("Type 0 for end the while loop:"))
while n!=0:
    def getm3(s,k):
        if(len(s)<7):
            return "Invalid String"
        if (k>len(s)):
            return "Not possible"
        mid=len(s)//2
        res=s[mid-(k//2):mid+(k//2)+1]
        return res

    s=input("String: ")
    k=int(input("Enter the middle values you want: "))
    print(getm3(s,k))
'''




#IMP.Q.
'''
s=input("Enter the string: ")
l=len(s)
print(s[::-1])
'''

#imp.Q.
#take a string from user and gave lower letters and after that upper letters
#Enter the string: DeePanShU
#eeanhDPSU

'''
def l(s):
    lower=""
    upper=""
    dig=""
    for ch in s:
        if ch.islower():
            lower+=ch
        
        else:
            upper+=ch
    return lower+upper
            
s=input("Enter the string: ")
print(l(s))
'''

#imp.q.


#take a string from user and gave lower letters and after that upper letters and after that digit.
#Enter the string: deepSh123
#deephS123
'''
def l(s):
    lower=""
    upper=""
    dig=""
    for ch in s:
        if ch.islower():
            lower+=ch
        elif ch.isdigit():
            dig+=ch
        else:
            upper+=ch
    return lower+upper+dig
            
s=input("Enter the string: ")
print(l(s))
'''





#IMP.Q.

#concatenate
#SELF but error

def c(list1, list2):
    con = []

    # Assuming both lists have the same length
    for i in range(len(list1)):
        con.append(list1[i] + list2[i])

    return con

list1 = int(input("Enter the number of elements in the list: "))
nlist1=[]
for i in range(list1):
    n=str(input("Enter number {}:".format(i+1)))
    nlist1.append(n)
print(nlist1)
list2 = int(input("Enter the number of elements in the list: "))
nlist2=[]
for i in range(list2):
    n2=str(input("Enter number {}:".format(i+1)))
    nlist2.append(n2)
print(list(nlist2))
output_list = c(list1, list2)
print("Expected output:", output_list)





#SAME by sir
'''
def c(list1,list2):
    res=[]
    if(len(list1)!=len(list2)):
        return "Invalid"
    else:
        for i in range(len(list1)):
            con=list1[i]+list2[i]
            res.append(con)
        return res
    
list1=input("Enter the value in list1: ").split()
list2=input("Enter the value in list2: ").split()
print(list1)
print(list2)
print(c(list1,list2))
'''




#IMP. Q.

#ERROR
'''
def reverse(n):
    return int(str(n)[::-1])
n=int(input("Enter the number: "))
print(reverse(n))
sum=n+reverse(n)
print(sum)
def fun(sum):
    if sum==0:
        return 1
    if sum==2:
        return fun(n-2)
    
    return (n%10)+fun(n//10)
print(fun(n))


def Digit(sum):
    if sum==0:
        return 0
    return (n%10)
print(Digit(n))
'''


#SAME BY SIR

'''
def p(n):
    if(n==n[::-1]):
        print(n[::-1])
        return len(n)
    else:
        num=int(n)+int(n[::-1])
        return p(str(num))


n=input("Enter: ")
print(p(n))
'''



#IMP. Q.

