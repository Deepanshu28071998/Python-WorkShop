###########################     SET     ######################################################
####################### set is an unoreded collection of heitroginious immutable items because elements of set are immutable. but set is mutable. 
#EX.
'''
s={1,2,1,4,5,6,1,2,5,4,7,8,5,9,2}
print(s)
'''



#EX.
'''
s={1,2,1,4,5,6,1,2,5,4,7,8,5,9,2}
print(s)
print(id(s))
#ERROR      #because we cannot define which value is first in set because set is unordered collection of data.
#print(s[0])
#print(id(s[0]))
s={1,2,1,4,5,6,1,2,5,4,7,8,5,9,2}
print(s)
print(id(s))
'''
#the adress of the set is changed if the set will be same.
'''
s={2,9,5,8,7,4,5,2,1,6,5,4,1,2,1}
print(s)
for e in s:
    print(e,end=' ')
    '''

#EX.
#Set gives us randomely elements0
'''
s={'s','a','b','ab',45,12,40}
print(s)
'''

#EX.
#empty set is not create we create dictonary type only.
'''
s={}
print(s)
print(type(s))
'''



########################### SET METHODS ################################
################## ADD(), UPDATE(), COPY(), CLEAR(), REMOVE(), POP(), DISCARD(), #######################
'''
s={1,4,2,5}
#ADDING ELEMENTS IN SET
s.add(3)    #adding elements in set
print(s)
s.add(8)
print(s)
#ERROR
#s.add(7,8,9)       #not allowed because it is mutable
#print(s)
s.add((7,9,8))
print(s)
#ERROR
#s.add({5,8,9})                 #not allowed because it is mutable
#print(s)
'''




#UPDATEING ELEMENTS IN SET
'''
s={1,4,2,5}
print(s)
s2={1,2,5,6}
s.update(s2)                #updateing elemts in set
print("after update:",s)
print(s2)
'''
'''
s1={1,4,2,5,6,7,8,9,10,11,12,15}
print("before",s1)
s2={100,200,500,600}
s1.update(s2)                #updateing elemts in set
print("after update:",s1)

s1.update([10000,200000,300000])
print(s1)
s1.update((1111,22222,3333,4444))
print(s1)
s1.update("niet")
print(s1)
print(s2)
'''



########### COPY METHOD ####33
####
#ex.
'''
s1={1,2,4,5,7,9}
s2=s1.copy()
print(s1)
print(s2)
s1.add(1000)
s2.add(1500)
print(s1)
print(s2)
print(id("s1",s1))
print(id("s2",s2))
'''

####################    CLEAR METHOD ########################

#EX.
'''
s1={1,2,4,5,7,9,2,4}
s1.clear()
print(s1)
'''

############### REMOVE METHOD #######################

#EX.
'''
s1={1,2,4,5,7,9,2,4}
s1.remove(2)
print(s1)
'''
#ERROR
#
#KeyError: 100
#
'''
s1={1,2,4,5,7,9,2,4}
s1.remove(100)
print(s1)
'''

#ERROR
'''
s1={1,2,4,5,7,9,2,4}
s1.remove()
print(s1)
'''

################### DISCARD METHOD ####################
#It is use in 'remove method gave throu an  error if the condition is not found but discard method is suspesor error (don't through error)  if the value is not found". 
#EX.
'''
s1={1,2,4,5,7,9,2,4}
s1.discard(100)
print(s1)
'''

#EX.
'''
s1={1,2,4,5,7,9,2,4}
s1.discard(1)
print(s1)
'''



################## POP METHOD ###########################
'''
s1={1,2,4,5,7,9,2,4}
print(s1)
s1.pop()            # In this pop remove the '1'.
print(s1)
s1.pop()
print(s1)           # In this pop also remove the 1st value '2'.
s1.pop()
print(s1)           #in this pop remove the value '4'

s2={1,2,4,5,7,9,'niet','a',4556,}
print(s2)
s2.pop()
print(s2)


s3={'dj',1,2,4,5,7,9,'niet','a',4556,}
print(s3)
s3.pop()
print(s3)
'''

#ERROR
'''
s3={'dj',1,2,4,5,7,9,'niet','a',4556,}
print(s3)
s3.pop(2)
print(s3)
'''


######################### UNION, INTERSECTION, DIFFERENCE, SUBSET, SUPERSET######################
#Union---> U
#Intersection--->
#Difference--->
#symmetric_difference--->
#SUB Set--->
#Super set--->

##### UNION ###########
'''
a={1,2,3,4}
b={2,3,5,6}
'''
'''
print(a.union(b))
u1=a.union(b)
print(u1)
print(a|b)      ### The vertical bar ( | ) -- also called the vertical line, vertical slash, pipe, pipe symbol or upright slash 
                    ### Bitwise OR (|)
'''
#I####### Intersection ######
'''
a={1,2,3,4}
b={2,3,5,6}
i1=a.intersection(b)
print(a.intersection(b))
print(a)
print(b)
print(i1)
'''
######Intersection_Update ###########
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
c={4,5,8,9,12,15}
d={1,2,3,4,5}
a.intersection_update(b)
print("intersection_update:",a)
d.intersection_update(b,c)
print("intersection_update:",d)
'''

# In intersection method we contain the intersection in a "variable", but in intersection_update method we can not use any "variable".


############## Difference ###################

#EX.
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
d=a.difference(b)
print("DIFF:",d)
print(a)
print(b)
'''



##################### Difference_update ########################

#EX.
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
a.difference_update(b)
print("DIFF:",a)
'''

'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
a.difference_update(b)
print("DIFF:",a)
b.difference_update(a)
print("newdiff:",b)
'''


'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
#a.difference_update(b)
#print("DIFF:",a)
b.difference_update(a)
print("newdiff:",b)
'''
# In difference we can store the diff. in a "variable', but in difference_update can not use any type of "variable".

###################Symmetric_diiference###############

#EX.
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
sd=a.symmetric_difference(b)
print("DIFF:",sd)
#b.difference_update(a)
#print("newdiff:",b)
'''


#################### Symmetric difference update ################

#EX.
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
a.symmetric_difference_update(b)
print("DIFF:",a)            #a={1,2,7,8,9}
'''

#EX.
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
a.symmetric_difference_update(b)
print("DIFF:",a)            #a={1,2,7,8,9}
b.symmetric_difference_update(a)
print("newdiff:",b)
'''



##################### ISDISJOINT(), ISSUBSET(),     ##########################

##### Isdisjoint()
#EX.
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
c={10,20,30}
print(a.isdisjoint(b))
print(a.isdisjoint(c))
'''

### if any element is comman then they are not DISJOINT so it is print "False", but if this condition any element is not comman then they are DISJOINT so it is print"True"...



###### Issubset ##############

#EX.

'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
c={1,2,3,10}
print(a.issubset(b))            #a is not a subset of b
print(c.issubset(b))            #c is not a subset of b
print(a.issubset(c))            #a is not a subset of c
print(c.issubset(a))            #c is not a subset of a
'''



###### Issuperset ##############

#EX.

'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
c={1,2,3,10}
print(a.issuperset(b))            #a is not a superset of b
print(b.issubset(c))            #b is not a superset of c
print(a.issubset(c))            #a is not a superset of c
print(c.issubset(a))            #c is not a superset of a
'''



#EX.

###### Issubset ##############

#EX.
'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
c={1,2,3,10}
print(set().issubset({1,2,3}))              #'set()' is a phy (fi) set
print({1,2,3}.issuperset(set()))
'''

###### Issubset ##############

#EX.

'''
a={1,2,3,4,5}
b={3,4,5,7,8,9}
c={1,2,3,10}
print(set().issuperset({1,2,3}))            #empty set is not a super set of {1,2,3}.
print({1,2,3}.issuperset(set()))            #{1,2,3} is a super set of empty set. 
'''

########## SUM,MAX,MIN,LEN,ANY,ALL ######################
'''
s={1,2,3,4,5}
s1={1,1,1,2,2,3,4,2,3,4,5,5,4,3}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
print(any(s))
print(all(s))
print(sum(s1))      # In it it is not consider any repitate value
print(max(s1))
print(min(s1))
print(len(s1))
print(any(s1))
print(all(s1))
'''


############ SET COMPREHENSION ###################
#syntax:-
'''
res={s for s in [1,2,3] if s%2}
print(res)
'''

#EX.
'''
s={1,2,3,(1,5,9)}
print(s)
'''
 ### Nested set ####
#EX.
'''
s={1,2,3,(1,5,9),"NIET"}
print(s)
'''
###### Frozenset #######
#EX.
'''
s={1,2,3,(1,5,9)}
print(s)
fs=frozenset(s)
print(fs)
'''
#In frozenset we have not repitated the values in the set.
'''
fs2=frozenset([5,4,5,4,7,8])
print(fs2)          #OUTPUT:-----           frozenset({8, 4, 5, 7})

'''

############################################### PART 2 ################################
###################### Dictionaries in python ##########################
########Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
####### Dictonary is a unordered collection of KEY:VALUE pairs.
# Dictonary is reprsent in { }.
# It is mutable
#
#
#
#

#EX.
'''
dic={"brand":"Ford","model":"mustang","year":"1964"}
print(type(dic))
print(dic)
'''
##EX.
#Duplicates Not Allowed
'''
dic={"brand":"Ford","model":"mustang","year":"1964","year":2020}        # In it it is only print 2020...
print(type(dic))
print(dic)
'''

#EX.
# How can we print a value with use of key.... 
'''
dic={"brand":"Ford","model":"mustang","year":"1964"}
print(type(dic))
print(dic["brand"])
'''

#EX.
#Empty dictonary
'''
d={}
print(d)
print(type(d))
#Dictonary use key:value
d1={1:"dj",2:"Deep",3:"DJAIN",4:"JAIN"}
print(type(d1))
print(d1)
'''
#EX.
'''
d1={1:"dj",2:"Deep",3:"DJAIN",4:"JAIN",'a':'"NIET"','b':'noida'}
print(type(d1))
print(d1)
'''
#EX.
#ERROR          #because spaicel symboles are not allowed in dictonary....
'''
d1={@:"MCA",1:"dj",2:"Deep",3:"DJAIN",4:"JAIN",'a':'"NIET"','b':'noida'}
print(type(d1))
print(d1)
'''

#EX.
#IMP
'''
d1={1:"dj","Deep":["DJAIN","JAIN"],3:(5,8,9),4:{9,7,5,1},'a':'"NIET"','b':'noida'}
print(type(d1))
print(d1)
'''

#EX.
#print values with the use of key.....
'''d1={100:1000,1:"dj","Deep":["DJAIN","JAIN"],3:(5,8,9),4:{9,7,5,1},'a':'"NIET"','b':'noida'}
'''
'''
print(type(d1))
print(d1)
print(d1[3])
print(d1[4])
print(d1[100])
#ERROR          # print(d1[Deep])
#Because Deep is string so we use in it ' '.
print(d1['Deep'])
'''
#keyerror       # print(d1[10])
#because key 10 is not in dictonary....

################# GET METHOD #################
'''
print(d1.get(1))
print(d1.get(10))       # It is not giving any error but 10 is not found in key, so it is giving us "None"....
'''

#IMP. Q.
'''
dict1={"name":"Mike","salary":8000}
temp=dict1.get("age")
print(temp)
#### (ANS). None
'''

#EX.
#How we add key and value in the dictonary....
'''
d={133:"Deepanshu Jain",93:"Ashutosh",44:"Gaurav"}
d[220]="Alok"
d[128]="Aashish"
print(d)
### Update method
d2={75:"Dhruv",273:"Gaurank"}
d.update(d2)
print(d)                ###    {133: 'Deepanshu Jain', 93: 'Ashutosh', 44: 'Gaurav', 220: 'Alok', 128: 'Aashish', 75: 'Dhruv', 273: 'Gaurank'}


# How we replace value with the use of key....
d[128]="Aman"
print(d)        # It replace the value with the use of key....

d3={93:"Salman",75:"Diksha"}
print(d.update(d3))    #### In it we can not update the value.  we firstly update the value and after that we print it so it is print the updated vaalue otherwise it print the None....    
d.update(d3)            ###### In it it firstly update the value and after that it print the value....  
print(d)
'''

############################ COPY METHOD ##################


#Ex.
'''
d={133:"Deepanshu Jain",93:"Ashutosh",44:"Gaurav"}
d2={75:"Dhruv",273:"Gaurank"}
d3={93:"Salman",75:"Diksha"}
'''
'''
d3=d2.copy()   # It copy d2 in d3 so d3 prints the value of d2....  
print(d3)
d3[100]=1500
d2[100]=5000
print(d2)           # In it add the key 100 and its value 5000...So, in print output is shows 5000--->  {75: 'Dhruv', 273: 'Gaurank', 100: 5000}
print(d3)           # In it add the key 100 and its value 1500...So, in print output is shows 5000--->  {75: 'Dhruv', 273: 'Gaurank', 100: 1500}                         
d4=d3
d4[200]="NIET" #In it d4=d3 so 200:"NIET" is add on both the dictonaries....    
print(d4)
print(d3)
'''
####### POP METHODS IN DICTIONARY ##############
#POP

#EX.
'''
d4.pop(75)
print(d4)
'''
#KeyError           #d4.pop(150) #ERROR
#print(d4)


# we use clear to remove all values....
'''
d4.clear()
print(d4) # It gaves us Empty dictonary {}
'''
'''
d2={75:"D",273:"g",522:"G",222:"r"}
d2.popitem() #Remove any one value Randomely
print(d2)       #{75: 'D', 273: 'g', 522: 'G'}
print(d2.popitem()) #In it we only print that item which is deleted or pop....   
print(d2)
'''
# In it it removes "ARBITRARY" Key:Value pairs


#======================================================================================================


'''
########### Keys #############
d2={75:"D",273:"g",522:"G",222:"r"}
print(d2.keys())


########### Values #############
print(d2.values())

########### Keys:Values #############
print(d2.items())
'''

##########OUTPUT------>
'''dict_keys([75, 273, 522, 222])
dict_values(['D', 'g', 'G', 'r'])
dict_items([(75, 'D'), (273, 'g'), (522, 'G'), (222, 'r')])
'''
#============================================================
#============================================================
############ FROM KEYS #############


#EX.

# fromkeys(seq,value)
#EX.
'''
seq=[1,2,3]
d=dict.fromkeys(seq,100)
print(d)
#OUTPUT----->  ##    {1: 100, 2: 100, 3: 100}
'''

#EX.
'''
seq=[1,2,3]
d=dict.fromkeys(seq,[100,200,300])
print(d)    # In it [100,200,300] assign as value for 1,2and3 all keys.....   
#We assign the same value for each key....
####OUTPUT---->  ##   {1: [100, 200, 300], 2: [100, 200, 300], 3: [100, 200, 300]}
'''
#EX.
# update the value in key....
'''
roll=[101,102,103]
att=dict.fromkeys(roll,"Present")
print(att)
att[102]="Absent"
print(att)
####OUTPUT--->
#   {101: 'Present', 102: 'Present', 103: 'Present'}
#   {101: 'Present', 102: 'Absent', 103: 'Present'}
'''

#Ex.
'''
roll=[101,102,103]
att=dict.fromkeys(roll,"Present")
print(att)
att[102]="Absent"
print(att)
att.setdefault(104)
print(att)          #{101: 'Present', 102: 'Absent', 103: 'Present', 104: None}
# It set the "None" in default key.
att.setdefault(105,"Present")
print(att) #{101: 'Present', 102: 'Absent', 103: 'Present', 104: None, 105: 'Present'}
# It set we set "Present" as a value for 105 key.
att.setdefault(102) # set default methodis not work if the value is already present.....   
print(att)
#OUTPUT--->ArithmeticError  # {101: 'Present', 102: 'Absent', 103: 'Present', 104: None, 105: 'Present'}
att[102]="Present"    # we change the value of key102 and print "Present".....  
print(att)
'''
#=============================================================
#=============================================================
############### NESTED DICTIONARY #########################

#EX.
#how we find a value of [key][key] Key into key
'''
d={1:"hi",'a':123,100:{2:"abc",'x':452,2.3:120},5.4:'python'}
print(d[100]['x'])
'''




###########

######### Length ##########
'''
d2={75:"D",273:"g",522:"G",222:"r"}
print(len(d2))
'''





