####################### DATA TYPES ######################################################
###### An entity which can store a data of specific type

#### Types of data ######
#(1). List
#(2). Tuple
#(3). Set
#(4). Dictonary
#(5). String


##### NOTE:- All these data type except string can stroe any of data (hetrogenious data).


############ (1). LIST###############
#######"List is a ordered collection of hytrogenious elements
'''
Listlist()---> []
l1=[2,4,5,...]
l2=[2,3,'A',2.54,4+3j,'NIET']


l=1,2,[3,4],[2.5,4.7]]
'''
#       -5 -4 -3 -2 -1 <----- Backward indexing

###
#       0 1 2 3 4  <----- forward indexing
######
#EX.
###Creation
'''
l=[]
print(type(l))
l2=list()
print(type(l2))
l3=[1,2,5,8,9]
print(l3)
print(type(l3))
l4=[1,2,'A',"niet","noida",5+4j,True,0,False]
print(l4)
print(type(l4))
'''
#ERROR
'''
l5=list(4,5,6,7)
print(type(l5))
'''
'''
l6=list(4)
print(type(l6))
'''
#CORRECT
'''
l7=list("niet")
print(type(l7))
'''


#####################

#Other EX.
###Creation
'''
l=[]
print(type(l),l)
l2=list()
print(type(l2),l2)
l3=[1,2,5,8,9]

print(type(l3),l3)
l4=[1,2,'A',"niet","noida",5+4j,True,0,False]
print(l4)
print(type(l4))
'''
#ERROR
'''
l5=list(4,5,6,7)
print(type(l5),l5)
'''
'''
l6=list(4)
print(type(l6),l6)
'''
#CORRECT
'''
l7=list("niet")
print(type(l7),l7)
'''


##########ADDITION of elements
###append() ---> add only one element at the end of list
###Inser() ---> add with using position
###extend() ---> add add many elements at the end


####(1). Append ----> list.append(n)
'''
li1=[1,2]
print(li1)
li1.append(5)
print(li1)
li1.append('A')
print(li1)
li1.append("niet")
print(li1)
li1.append(5+2j)
print(li1)
li1.append(True)
print(li1)
'''


###(2). Insert (index,value)

#EX.
'''
li1= [1, 2, 5, 'A', 'niet', (5+2j), True]
li1.insert(2,100)
print(li1)
li1.insert(0,45)
print(li1)
li1.insert(4,"Deepanshu")
print(li1)
'''


#EX.
'''
li1=[45, 1, 2, 100, 'Deepanshu', 5, 'A', 'niet', (5+2j), True]
print(li1)
li1.insert(12,"Jain")   #If in list value are write 0 to 9 but we can added "jain" at 12th possition so it gave "jain" at end of the list.
print(li1)
li1.insert(100,"NIET")
print(li1)
li1.insert(50,"DJ")   #In this case we already added a value in the list in the last so if we added "DJ" at the 50th posion so it gave "DJ" at the end of the list.
print(li1)
            #WRONG              li1.inser(index,"noida")
li1.insert(-4,"Delhi")
print(li1)
li1.insert(-50,"Mallesh Sir")   #If in list value are write -1 to -13 but we can add "Mallesh Sir" at -50th position so it gave "Mallesh Sir" at the begning of the list.
print(li1)
li1.insert(-100,"PM")
print(li1)      #In this case we already added a value in the list in the last so if we added "PM" at the -100th posion so it gave "PM" at the begning of the list.
li1.insert(-20,"AMAN")
print(li1)      #SAME CASE
li1.insert(-2,"mca")
print(li1)      #Add in the -2th position.
li1.insert(150,2500)
print(li1)
li1.append(5000)
print(li1)
#ERROR                           li1.append(45,25) #In append only one element is accepeted at a time.ctime
#print(li1)

#NESTED LIST
#Ex.
li1.append([45,25])
print(li1)

#EX.
li1.append([[4,5,6],[5,6,7],[10,11,12]])
print(li1)


li1.append([25,78][1]) #In the list [25,78] we only added 1st positon value in the pre.list.
print(li1)
#In it append the value to take the place from the next value to take it into the prev. list


li1.extend([100,200,300,400]) #It take each element is a seprate index.
print(li1)
li1.extend([45,25,78])          #In it 
print(li1)
'''
####Append method well add the sequence of elements at the end of the list in a single index. 
####Where extened method sequence of elements at the end of the list in individuale in the sence.
######
######
######

#EX.
'''
print(li1[0])
print(li1[5])
print(li1[7][2]) #In it the value writen in 7th position "Deepanshu" and write the 2nd element in "Deepanshu" is "e". So, it is print--->e.
print(li1[7][4])
print(li1[11])

#Error              print(li1[11][0])    #Because in the list at the 11th position complex number are writen so it is not giving any elements in it.
print(li1[-10])
print(li1[-2])
print(li1[-9])
print(li1[-10][1])
print(li1)
print(100 in li1)
print(200 in li1)
print(500 in li1)
print(200 not in li1)
print(100 not in li1)
print(500 not in li1)
'''



################## UPDATE ##################################
#WE change the value in the     is called the updation
'''
li1=['AMAN', 'PM', 'Mallesh Sir', 45, 1, 2, 100, 'Deepanshu', 5, 'A', 'niet', (5+2j), 'Delhi', True, 'Jain', 'mca', 'NIET', 'DJ', 2500, 5000, [45, 25], [[4, 5, 6], [5, 6, 7], [10, 11, 12]], 78, 100, 200, 300, 400, 45, 25, 78]
li1[0]='Gaurav'
print(li1)
li1[20][1]=250          #It update the value of [45,25] and write [45,205]. 
print(li1)

#ERROR     li1[0,5]=45,"PK"
#print(li1)
'''
#################### DELETION #######################################################
'''
pop() ---> last element
pop(arg)
remove()
clear()
del()
'''
'''
li1=['Gaurav', 'PM', 'Mallesh Sir', 45, 1, 2, 100, 'Deepanshu', 5, 'A', 'niet', (5+2j), 'Delhi', True, 'Jain', 'mca', 'NIET', 'DJ', 2500, 5000, [45, 250], [[4, 5, 6], [5, 6, 7], [10, 11, 12]], 78, 100, 200, 300, 400, 45, 25, 78]
print(li1)
print(li1.pop()) #print the last element.
li1.pop()
print(li1) #POP() remove the list element from the list.
print(li1.pop())
print(li1.pop(0))
print(li1)
li1.pop(-1)
print(li1)
print(li1.pop(-5))
print(li1)
#ERROR                                          print(li1.pop[-5][1])
#print(li1.pop

'''


############ REMOVE #############
'''
li1=['PM', 'Mallesh Sir', 45, 1, 2, 100, 'Deepanshu', 5, 'A', 'niet', (5+2j), 'Delhi', True, 'Jain', 'mca', 'NIET', 'DJ', 2500, 5000, [45, 250], 78, 100, 200, 300]


li1.remove(2500)     #It remove the particular value "2500" from the list.
print(li1)
li1.remove(100)
print(li1)
li1.remove(100)
print(li1)
'''
#ERROR
#It can't work because 4 is in nested list.
'''
l=[1,2,3,[4,5,6]]
l.remove(4)
print(l)
remove(l,4)
print(l)
'''
#ERROR        li1.remove(250) #Because we cann't remove the value from the nested list.
#print(li1)
#ERROR              li1.remove(x)           #because 'x' is not in this list.
#print(li1)



######################## H.W. ############################################
#Empliment user defined remove method in the list, which remove specified element in the list.
#Syntax remove(seq,val)


#(1). if value is present
#(2). if value is not present.


############################ (4). Index ########################################################
'''
l=[1,2,3,4,5,6]
print(l.index(4))
#ERROR              print(l.index(250))             #because 250 value is not present in the given list.       
#ERROR              print(l.index('a'))             #because 'a' value is not present in the given list.       
'''
'''
l=[1,2,4,2,4,5,4,2,6,8,10]
print(l.index(4))   #It gave output '2' because 4 is firstly present at 2nd position.
print(l.index(8))   #It gave output '9' because 8 is firstly present at 9th position.
print(l.index(100)) #It gave error because 100 is not present in the list.
'''



####################### COUNTN ########################################
'''
l=[1,2,4,2,4,5,4,2,6,8,10]
print(l.count(4)) #It count the value of 4 is in the list... OUTPUT ---> 3
print(l.count(2))
print(l.count(10))
print(l.count(100))     #It gave 0 as count the value of 100 in the list because 100 is not in the list.
'''

####################### CLEAR ########################################
'''
l=[1,2,4,2,4,5,4,2,6,8,10]
l.clear()       #All the value vanished from the list. 
print(l)        #list is print a empty list.
#ERROR          l.pop()         #Because list is already empty so we can't remove any value from the empty list.
#print(l)
l.append(45)    #append 45 in the list
print(l)
l.remove(45)
print(l)
'''

###################### Del ########################
'''
l=[1,2,3]
print(l)
#ERROR      del(l)          #because in del() we give the value is lien in the list. It is deleted fromthe memory so itis not shown.   
print(l)
l=[1,2,3]
l.clear()
print(l)        #it clear aal the value fromthe 'l' list.
'''



####################################    PART 2      ##########################################################
#############################################################################################
#################################################################################
######################
############################################# COPY #################################################################
#EX.
###### Shallow copy ###########
'''
l1=[1,2,3,4]
l2=l1.copy()
print(l1)
print(l2)
print(id(l1))
print(id(l2))
'''

######## deep copy ############
'''
l3=[1,2,3,4,5]
l4=l3
print(l3)
print(l4)
print(id(l3))
print(id(l4))
#l4=l1
print(l4)
l3.append(150)
print(l3)
l4.append(100)
print(l4)

l4[0]=4
print(l4)
'''

#Self try:
'''
if l1==l2:
    print("l1==l2")
else:
    print("l1!=l2")
'''

'''
l1=[2,4,6,8]
l1=l2
print(l1)
print(l2)


l1.append(100)
l2.append(200)
print(l1)
print(l2)
'''
##EX.


'''
l1=[2,4,6,8]

print(l1)
print(l2)


l1.append(100)
l2.append(200)
print(l1)
print(l2)
'''
########################################################## SORT ######################################################
##In sort method only numbers can be applied in the list...
#EX.
'''
l1=[12,51,45,32,10,21]
l1.sort()
print(l1)
l2=[12,98,-25,32,-14,45]
l2.sort()
print(l2)
'''
#ERROR
'''

l3=[2,"DJ","Deep","Deepanshu jain"]     #In it not use numebrs and string both together.
l3.sort()
print(l3)
'''
'''
l=["AB","BA","noida","ab","king"]       #It works because in it only string can work. 
print(l)
l.sort()
print(l)


l=["A","B","R","E","Z"]                 #It works because in it only string can work. 
l.sort()
print(l)
'''




##
##
#################################################### REVERSE ################################################################
##In it we use numbers aas well as alphabets and string....

'''
l1=[12,51,45,32,10,21]
l1.reverse()
print(l1)
l2=[12,98,-25,32,-14,45]
l2.reverse()
print(l2)
l3=[2,"DJ","Deep","Deepanshu jain"]
l3.reverse()
print(l3)
'''

#
##################### Built in function #########################
'''
#sum
l=[1,2,4,5,8,9]
print(sum(l))
#max
print(max(l))
#min
print(min(l))
#any
print(any(l))                   #atlest any one value is non zero it is "TRUE".   
#all
print(all(l))                   #all value are non zero so it is "TRUE".
#length---> len()
print(len(l))
'''
'''
l=[1,2,4,False,8,9,0]         
print(max(l))
print(min(l))               #In it False comes before the zero so it prints "False".

li=[1,2,0,4,False,8,9]
print(max(li))
print(min(li))          #In it 0 comes before the "False" so it prints "0".
'''

#Check the length of the given lists.
'''
l=[1,2,3]
l1=[4,5]
l2=l+l1
print(len(l2))
'''
'''
l=[2,5,4]
l2=l*3              #the list l is repeted 3 times.
print(l)
print(l2)
l3=l+l2
print(l3)
l4=l2*2
print(l4)
'''




'''
l=[1,2,3,4,5]
l1=['a','hi',4512]
l.append(l1)
print(len(l))
l1.extend(l)
print(len(l1))
'''




######################### SLICING A LIST ##########################
#SLICE OPERATION IS USED TO POINT SPECIFIC RANGE OF ELEMENTS FROM THE LIST..
#Slice operation is performed on list with the use of colon (:)...

l=[2,1,5,4,9,7,8,13,15,11,3]
'''
print(l)
print(l[0:10:1])
print(l[0:11:2])
print(l[2:9:1])
print(l[0:8])
print(l[:10])
print(l[1:8:3])

'''
'''
print(l[9:2:-1])
print(l[10:3:-3])
#Error      print(l[10:3:3])            #Because we not go to 10 to 3 in ascending order
print(l[-2:-10:-2])
print(l[len(l)-1:0:-1])
print(l[len(l):-1:-1])
'''
'''
print(l[-10:-2:-1])
print(l[-2:-10:-1])
print(l[0:10])
print(l[2:6])
print(l[-4:-2])
print(l[-6:-1])
'''
print(l[::2])




