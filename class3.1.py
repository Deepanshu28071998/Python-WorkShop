########Itration Statement#########
#(a).
#FOR:-
#Syntax:-
'''
for i in squence:
        statement1

'''
#Error

'''for i in [n,i,e,t]:
    print(e)
'''


#range(start,stop,step)

#ex.
'''
range(0,10,1)
        output:-  0,1,2,3,4,5,6,7,8,9






range(6,28,2)
        output:-             6,8,10,12,14,16,18,20,22,24,26
        '''
#1.
'''
for i in range(0,10,1):
    print(i)
'''

#2
'''
for i in range(6,28,2):
    print(i)
'''
#3
'''
for i in range(0,500,5):
    print(i)

'''
###Negative
#4.
#######+ve<stop
#######-ve>stop
'''
for i in range(10,0,-1):
    print(i)

for i in range(20,0,-3):
    print(i)


for i in range(10,-1,-1):
    print(i)


'''
#range(1,15):
#           output:-            1,2,3,.....,14
'''
for i in range(1,15):
    print(i)
'''
'''
for i in range(-5,0):
    print(i)
'''

#range(-5,-10):
#Error
'''
for i in range(-5,-10):
    print(i)
'''
#correct
'''
for i in range(-5,-10,-1):
    print(i)
'''
#range(10):
#           output:-    0,1,2,....,9
'''
for i in range(10):
    print(i)
'''
#error
'''
for i in range(10,0):
    print(i)
'''
#correct
'''
for i in range(0,10):
    print(i)
'''
#error
'''
for i in range(-10):
    print(i)
'''
#correct
'''
for i in range(-10,10):
    print(i)
'''
#Reprecentation of inclusive and exclucive:-
#Another methods:
#[2,8]
'''
for i in range(2,9):
    print(i)
    '''
#(2,8)
'''
for i in range(2,8):
    print(i)
    '''
#[2,8)
'''
for i in range(2,8):
    print(i)
    '''
#(2,8]
'''
for i in range[3,9):
    print(i)
'''
#write a prog. to print all the even numers and odd numers in the given range y the user:-
'''
start = int(input("Enter start: "))
end=int(input("Enter end: "))
print("Even numers")
for n in range(start,end):
    if (n%2==0):
        print(n)
print("Odd numers")
for n in range(start,end):
    if (n%2!=0):
        print(n)
'''


###This prog. is same as prv. but in this case all values print including last value:-
'''
start = int(input("Enter start: "))
end=int(input("Enter end: "))
print("Even numers")
for n in range(start,end+1):
    if (n%2==0):
        print(n,end=",")
print("\nOdd numers")
for n in range(start,end+1):
    if (n%2!=0):
        print(n,end=",")

'''
########H.W.###########(1).
#Write a prog. to find the diff. of some of even numers and some of odd numers to give a including range.







##Write a prog. to gunrate a table.
'''
n=int(input("Enter the numer: "))
for i in range(1,11):
    print(n,'*',i,'=',n*i)
'''
'''
n=int(input("Enter the numer: "))
for i in range(1,11):
    print(f"{}*{} = {}".format(n,i,n*i))
'''


#####
'''
n= int(input("Enter a numer: "))
for i in range(1,n):
    if(i%3==0):
        print(i+5)
    else:
        print(i-3)
'''
#if FOR is fail else work on it:
'''
n= int(input("Enter a numer: "))
for i in range(1,n):
    if(i%3==0):
        print(i-2)
else:
    print(i+5)
'''
#correct:
'''
n= int(input("Enter a numer: "))
for i in range(1,n):
    if(i%3==0):
        print(i-2)
    else:
        print(i+5)

'''


#Write a prog. to given number is prime or not.

'''
n=float(input("Enter the number: "))
if n>1:
    for i in range(2,int(n/2)+1):
        if(n%i)==0:
            print(n," is not a prime number.It is divided by",i)
            break
    else:
        print(n,"is a prime number.")
else:
    print(n," is not a prime number.")

'''


#Sir methods:-
'''
n=int(input("Enter value: "))
print("Factors of" ,n,"are:")
flag= True
for i in range(2,(n//2)+1):
    if(n%i==0):
        flag=False
        
if (flag):
    print("Prime")
    
else:
    print("not Prime")
'''
#Another methods use by the sir:
'''
n=int(input("Enter value: "))
print("Factors of" ,n,"are:")
flag= True
for i in range(2,(n//2)+1):
    if(n%i==0):
        flag=False
        #print("not Prime")
if (flag):
    print("Prime")
    
else:
    print("not Prime")

'''
#Another methods use by the sir:
'''
n=int(input("Enter value: "))
print("Factors of" ,n,"are:")
flag= True
if n>1:
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            flag=False
            
    if (flag):
        print("Prime")
    
else:
    print("not Prime")
'''
#Another methods use by the sir:
'''
n=int(input("Enter the value: "))
cnt=0
for i in range(1,n+1):
    if(n%i==0):
        cnt+=1
if (cnt==2):
    print("Prime")
else:
    print("Not Prime")
'''

########NESTED LOOP############
#(1).
'''
for i in range(5):
    for j in range(5):
        print(i,j)
'''
#(2). Self Try
'''
n=int(input("Enter the value: "))
m=int(input("Enter the value: "))
for i in range(n+1):
    for j in range(m+1):
        print(i,j)
'''
#(3). y sir
'''
for i in range(5):
    for j in range(5):
        if (i+j==5):
            print(i,j)
'''

##########H.W. #########
#write a prog. to print all commas seperated pairs those sum is divisile  by 3 and 5.
'''
for i in range(5):
    for j in range(5):
        if (i+j)%3=0 and (i+j)%5=0:
            print(i,j)
'''

##########H.W.###########
#write a prog. to print all commas seperated pairs those sum is a prime number.(Start and stop should e taken from the user.





    
###Sir done this:
'''
for i in range(5):
    for j in range(5):
        if (i+j==5):
            print(i,j)
        else:
            print(i+j)
'''

########################WHILE LOOP########################################
#G.STATEMENT
#while(condn):
#   S1
#   S2
#   change in val
#S3
#ex.
'''
i=0
while (i<5):
    print(i)
    i+=1
'''


'''
i=0
for (i<5):
    print(i)
    i+=1
'''



#write a program to find how many digits in the given num.
'''
n=int(input("Enter a Num: "))
cnt=0
while n!=0:
    #r=n%10
    #n//=10
    cnt+=1
    n//=10
print(cnt)
'''
'''
n=int(input("Enter a Num: "))
cnt=0
while n!=0:
    #r=n%10
    #n//=10
    cnt+=1
    r=n//10
print(cnt)
print("Digits in the",n,"is",cnt)
'''
            

############H.W.#########################
#write a prog. to find num. of non zero digits in the given num..
#write a prog. to find dum of digits of given num.
'''
n=int(input("Enter a Num: "))
sum=0
while n!=0:
    sum+=n%10
    n//=10
print(sum)
#print("Digits in the",n,"is",cnt)

'''
######H.W.#####
#Write a program to sum of even digits in the given num.:
#Write a program to sum of odd digits in the given num.:
#write a program to find the diff. of 'sum of even and odd' digits.

#################################################################################################################################################################################################
#################################################################################################################################################################################################
#################################################################################################################################################################################################
#################################################################################################################################################################################################
                        #PART


#NESTED WHILE loop:
##Doule while loop:-
#(1).
'''
i=0
while(i<5):
    j=0
    while(j<5):
        print(i,j)
        j+=1
    i+=1
'''

#While And For:-
'''
i=0
while(i<5):
    for j in range(5):
        print(i,j)
    i+=1

'''
#While And For And IF:-

'''
i=0
while(i<5):
    for j in range(5):
        if ((i*j)%3==0):
            print(i,j)
    i+=1
'''

####for while:-
'''
for i in range(10):
    j=1
    while (j<i):
        print(j)
        j+=1
'''
#####for while:-
#####to understand how it is work:-
'''
for i in range(1,10):
    j=0
    while (j<i):
        print(j)
        j+=1
    print("---")
'''

#########JUMPING STATEMENT##########
##J.S. are used with in the loop along with code.
#G.Syntax:-
#Loop{
#    Condition:
#        break
#    }
#
#######Syntax:-
'''
for i in range(10):
    if(i==5):
        print(i+5)
        break
    print(i)

'''

####There are three type of jumping statements:-
#(1).BREAK
#(2).CONTINUE
#(3).PASS
####
####(1). BREAK:----->when we have break statement in our program we get out of the loop.
#Termination of the loop excuation.
#break----> break= loop will e executed till that iteration if condfition in not true.
#- Break statement: Terminates the loop prematurely and resumes the execution of the code outside the loop.
#break
'''
print("enter the loop")
for i in range (10):
    if (i==5):
        print(i+5)
        break
        print("after break")
    print(i)
print("out of the loop")
'''
#####(2).continue:----> When we have continue sta. in our prog. control comes eging of the loop. the statements after continue will be excicutaed........
####Continue statement: Skips the remaining statements in the current iteration of the loop and resumes execution at the next iteration.
##Continue= execute all the iteration except for while condition is true.
'''
print("enter the loop")
for i in range (10):
    if (i==5):
        print(i+5)
        continue
        print("after continue")
    print(i)
print("out of the loop")
'''

######(3). Pass:----->Acts as a placeholder statement that does nothing, used to represent an empty block of code or as a temporary placeholder for code that will be added later.
######PASS:-----> No Change.

'''
print("enter the loop")
for i in range (10):
    if (i==5):
        print(i+5)
        pass
        print("after pass")
    print(i)
print("out of the loop")
'''
'''
def register():
    pass
def login():
    pass
def logout():
    pass
'''


###
###################patterns in python#########################################
####*****PATTERNS IN PYTHON###########
'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        print('*',end=" ")
    print()
'''
####Extra method copy form 'GEEKSFORGEEKS' on INTERNET.
'''
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, 5):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ",end=" ")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
pypart(n)
'''
######PRINT STARS ONLY ON BORDRS NOT IN SIDE:
'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''


########PRINT STARS ONLY MAKE AS "X":

'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i+j==row-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''





##############PRINT STARS
#****
# ***
#  **
#   *
'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i<j: #or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()

'''

##########PRINT STARTS

'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i+j==row-1 or i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''


###########PRINT STARTS
#*         
#* *       
#* * *     
#* * * *   
#* * * * *

'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i>=j:
        #i+j==row-1 or i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''

###########PRINT STARTS
'''
* *       
  * *     
    * *   
      * * 
        *
        '''
'''

row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i==j-1:
        #i+j==row-1 or i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()

'''


############
'''
*       * 
* *   * * 
*   *   * 
* *   * * 
*       * 
'''
'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i+j==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()

'''



###########
'''
* * * * * 
  *   *   
    *     
  *   *   
* * * * *
'''
'''


row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i+j==row-1 or i==0 or i==row-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()

'''

############
'''
*       * 
* *   *   
* * *     
* * * *   
* * * * *
'''
'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i>=j or i+j==row-1:
        #i+j==row-1 or i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''





###########
'''
*         
* *       
*   *     
*     *   
* * * * *
'''
'''

row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i==row-1 or j==0:
        #i+j==row-1 or i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''



############
'''
*       * 
* *     * 
*   *   * 
*     * * 
* * * * * 
'''
'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or i==row-1 or j==0 or j==row-1:
        #i+j==row-1 or i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''


#########
'''
*       * 
* *     * 
*   *   * 
*     * * 
*       * 
'''
'''
row=int(input("Enter num. of Rows "))
col=int(input("Enter num. of Columns "))
for i in range(row):
    for j in range(col):
        if i==j or j==0 or j==row-1:
        #i+j==row-1 or i==0 or i==row-1 or j==0 or j==col-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
  
    print()
'''





#########








########





########
