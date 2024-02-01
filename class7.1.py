                    #### DAY 7 #####
######################### SLICING A LIST ##########################
#SLICE OPERATION IS USED TO POINT SPECIFIC RANGE OF ELEMENTS FROM THE LIST..
#Slice operation is performed on list with the use of colon (:)...
                #### Part 2 ####

#EX.
'''
l=[2,1,5,4,9,7,8,13,15,11,3]
print(l[::2])
print(l[::-1])
print(l[1:6:3])
'''

#EX.
'''
n1==['Python','sarkar','DJ','om']
n2=n1



'''



############################# Traversal #############################
#EX.
'''
nl=[[1,2,3],[4,5,6],[7,8,9]]
print(nl)
l=[1,2,4,8,9,6]
for e in l:
    print(e,end=" ")
    
'''

#EX.
'''
nl=[[1,2,3],[4,5,6],[7,8,9]]
print(nl)
for sub in nl:
    print(sub)
'''

####################### Traversal of Nested List #############################
#EX.
'''
nl=[[1,2,3],[4,5,6],[7,8,9]]
print(nl)
for sub in nl:
    for e in sub:
        print(e,end=' ')
    print()
'''



#EX.
'''
l=[]
nl=int(input("enter no of sub lists in list: "))
for i in range(nl):
    n=int(input("enter the no of elements in sublist-{}".format(i+1)))
    sub=[]
    for j in range(n):
        e=int(input("enter a sublist[{}][{}]".format(i,j)))
        sub.append(e)
    l.append(sub)
    print(l)
print(l)
'''


#EX.
'''
rows=int(input("enter rows: "))
cols=int(input("enter columns: "))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        e=int(input("enter: "))
        row.append(e)
    matrix.append(row)
print(matrix)
'''

#EX.
'''
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
m=[]
for i in range(r):
    row=[]
    for j in range(c):
        n=int(input("Enter the value: "))
        row.append(n)
    m.append(row)
print(m)
'''



#EX.
'''
rows=int(input("enter rows: "))
cols=int(input("enter columns: "))
matrix=[]
for i in range(rows):
    #row=[]
    for j in range(cols):
        row=list(map(int,input().split()))
        #row.append(e)
    matrix.append(row)
print(matrix)
'''


#EX.
#create a matrix in one row and no limit coloumns.
'''
rows=int(input("enter rows: "))
#cols=int(input("enter columns: "))
matrix=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrix.append(row)
print(matrix)
'''



###Write a prog. to perform addition of matrises.
'''
rows=int(input("enter rows in matrix: "))
cols=int(input("enter columns in matrix: "))
print("Enter elements in matrix-A")
matrixA=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixA.append(row)
print("enter elements in Matrix-B:")
matrixB=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixB.append(row)
print(matrixA)
print(matrixB)
'''

#EX.
'''
rows=int(input("enter rows in matrix: "))
cols=int(input("enter columns in matrix: "))
print("Enter elements in matrix-A")
matrixA=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixA.append(row)
print("enter elements in Matrix-B:")
matrixB=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixB.append(row)
print(matrixA)
print(matrixB)
print("Enter elements in matrix-C")
matrixC=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        e=matrixA[i][j]+matrixB[i][j]
    #row=list(map(int,input().split()))

        row.append(e)
    matrixC.append(row)
print(matrixC)
'''


#### H. W.###############
###Take two matrix and multiply them
'''
rows=int(input("enter rows in matrix: "))
cols=int(input("enter columns in matrix: "))
print("Enter elements in matrix-A")
matrixA=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixA.append(row)
print("enter elements in Matrix-B:")
matrixB=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixB.append(row)
print(matrixA)
print(matrixB)
print("Enter elements in matrix-C")
matrixC=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        e=matrixA[i][j]*matrixB[i][j]
    #row=list(map(int,input().split()))

        row.append(e)
    matrixC.append(row)
print(matrixC)
'''

#### H.W.###############

####Wrong

'''
rows=int(input("enter rows in matrix: "))
cols=int(input("enter columns in matrix: "))
print("Enter elements in matrix-A")
matrixA=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixA.append(row)
print("enter elements in Matrix-B:")
matrixB=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrixB.append(row)
print(matrixA)
print(matrixB)
print("Enter elements in matrix-C")
matrixC=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        e=matrixA[i][j]+matrixB[i][j]
    #row=list(map(int,input().split()))

        row.append(e)
    matrixC.append(row)
print(matrixC)
'''


#EX.
'''
rows=int(input("enter rows: "))
#cols=int(input("enter columns: "))
print("
matrixA=[]
for i in range(rows):
    #row=[]
    #for j in range(cols):
    row=list(map(int,input().split()))
        #row.append(e)
    matrix.append(row)
print(matrix)
'''

#EX.
### Sumof diagonals values.
'''
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of coloumns: "))
print("enter elements in Matrix: ")
matrix=[]
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
trace=0
for i in range(rows):
    for j in range(cols):
        if(i==j):
            trace+=matrix[i][j]
print("Trace of Matrix:",trace)
'''


#EX.
###sum of both diagnoals
'''
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of coloumns: "))
print("enter elements in Matrix: ")
matrix=[]
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
trace=0
for i in range(rows):
    for j in range(cols):
        if(i==j or i+j==rows-1):
            trace+=matrix[i][j]
print("Trace of Matrix:",trace)
'''


#####H.W.################
## Write a program. to verify given matrix is super matrix or not....
###diffrence of condition
#(1). if difference of sum of forwared diagnoal and sum of backword diagnoal is zero then It is super matrix.
#(2). if sum of farward diag.> sum of backward diag. matrix is mega matrix.
#(3). if sum of farward diag.<sumof backward diag. matrix is micro matrix.


######## H.W.

#Write a prog. to find the maximun and minimum value without using built in function.


#############H.W.
#Write a prog. to read a nested list and to return or to print a sublist whoese sum is maximum

########H.W.

#Write a prog. to print asublist of length k (k is given by the user) whose sum is minimum....

'''
l=[2,9,3,1,4,5,6]
k=int(input("Enter the limit of the list"))
for i in range(l[0],len(l)-1,k):
    row=[]
    row.append(i)
print(row)
'''



################################## LIST COMPREHENSION ######################################
#(1). [output_expr      input_seq           variable condition ]
#(2). seq= [1,3,5,2,4,7,9,4,6,7,8,11,13]
    # even= [ for val in seq:   if val%2==0]
#EX.

###find the even values from the given list
'''
seq= [1,2,3,4,5,6,7,8,9,11,15,14,16,18]
even=[val for val in seq if val%2==0]
print(even)
'''


#EX. 

####Find the squares of each element in the list.
'''
seq= [1,2,3,4,5,6,7,8,9,11,15,14,16,18]
squares=[val**2 for val in seq]
print(squares)
'''


#EX.

###Find the even and odd values from the given list....
'''
seq= [1,2,3,4,5,6,7,8,9,11,15,14,16,18]
even=[val for val in seq if val%2==0]
odd=[val for val in seq if val%2!=0]
print(even)
print(odd)
'''

#EX.

##Find the squareroot of the given list.
'''
seq= [1,2,3,4,5,6,7,8,9,11,15,14,16,18]
squareroot=[val**0.5 for val in seq]
print(squareroot)
'''

#EX.

#Find the factorial of all elements in given list



########## H.W. #########
##By using list comprehension extract all prime numbers froma given list.



############################################################################################
###############################################################################################
######################################### PART 2 #######################################
####################################### TUPLES ###########################################
###########################################################################################
##########################################################################################
################################################################################################
#################################################################################################
############################################################################################
####################
#Tuple is immutable.
#tuple is a ordered collection of hitroginius function.
#Tuple can be 
#
#
#EX.
'''
a=tuple()
t=()
b=(4,2,5,8)
print(type(a))
print(type(t))
print(type(b))
'''
#EX.
'''
c=2,4,5,8,9
print(c)
print(type(c))
'''
#EX.

#ERROR          #because tuple can not be changed at the excecution time...
'''
t=(1,2,3.45,'python',65,4)
t[1]=6.25
print(t)
'''
#ERROR                  #

#
#Q).
'''
t=(21,51,32,32,51,51,10)
print(t.count(t[t.index(51)+1]))
'''

#EX.
'''
t=(1,23,65,12)
print(sum(t))
print(max(t))
print(min(t))
print(all(t))
print(any(t))
print(len(t))
'''
#IMP. Q.).
'''
t=(1,2,3)
t1=((4,5,6,7))
t2=t+t1
print(t2)
print(len(t2))
'''
#IMP. Q.).
'''
t=(1,2,3)
t1=((4,5,6,7),10,5,3,4)
t2=t+t1
print(t2)
print(len(t2))
'''
#EX.
###Concatenation of Tuple (+)
#Repetition of Tuple (*)
#Membership operators on Tuple (in,not in)
'''
t=(1,2,3)
t1=(4,5,6)
print(t+t1)


'''



#################################################################
############ SLICING A TUPLE ############################
#This slicing is same as list slicing...





####################################
#################### NESTED TUPLE ############################################

#
#
#ex.
'''
t=(1,2,3.11,(4,5),6,('hi','hello'),7)
print(t)
print(t[5][1])
'''
#ERROR  print(t[5][1][3])
#ERROR  print(t[4][2])
'''
t=(21,34,'hi',(56,'abc','python',124),6,24)
print(t[3][::-2])
'''
'''
t=(1,2,4,3,6,5,10,9)
t1=tuple([i**2 for i in t[::2]])
print(t1)
'''



######################LET's START CODING ########################################

#WRONG
'''
a=1 ,2 ,3 ,6
b=0 ,5 ,7
c=(a+b)
print(c)
c.sort()
print(c)
'''

#EX.
'''
l=[1,2,4,2,1,5,7,4,5]
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)
'''

'''
l=[1,2,4,2,1,5,7,4,1,2,4]
res=[]
for i in l:
    if i not in res and l.count(i)%2==1:
        res.append(i)
print(res)
'''





##################
###########
########
#
#
##
#
#

##
#

##

#
###

#
#
#
#
##
#
#

###
#
#
#
#
#
