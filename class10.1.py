################## FILE HANDLING ###############
##### file:-
#### File is a named location on a disk with related information.

#(1) Opening a file


#open(filename,mode)  ----> open("file.txt",r)

## filename --->(i) relative path   (ii) absolute path
## mode ----> (i) r-read mode (ii) w- write mode   (iii) a- append mode
# r+ -> read and write
# w+ -> write and read

# genral syntax:-->      with open(file, mode) as f:
#              # (i) READ MODE:-    #

'''
file=open("E:\samplefile.txt.txt",'r')
print(file)             #print the file information in encoding..... 
info=file.read(5)       #will read 5bits
print(info)
print("cursor position:",file.tell())
file.seek(5)
info2=file.read(10)     #will read 10 bits
print(info2)
print("cursor position:",file.tell())
'''
'''
line=file.readline()    #will read next line
print(line)
line2=file.readline()   # will read next line
print(line2)
lines=file.readlines()  #Read all the remaining lines as a list with comma(,) separated
print(lines)
l=file.read()       #Read all the file
print(l)    
file.close()
'''
#file.read()--> reads complete information from the file.
#file.read(n)--> reads n bytes of information from the file.
#file.readline()--> reads single line
#file.readlines() --> reads remaining into n lines return left of line... Reads all the lines at once and returns them as a string with \n\r separated.
'''
file=open("E:\samplefile.txt.txt",'r')
# print(file)
info=file.read(5)
# print(info)
info2=file.read(10)
# print(info2)
line=file.readline()
# print(line)
# line2=file.readline()
# # print(line2)
# lines=file.readlines()
# # print(lines)

print(info2)
print("cursor position:",file.tell())
data=file.read(10)
print(data)
file.close()
'''
#####====================#####
#              # (ii). WRITE #      #
'''
file=open("mca_niet.txt",'w')           #it creates a new file in the foldar...
# print(file)
file.write("NIET Welcome You\n")           #It write the text in the file...
file.write("We are MCA")
file.close()
#change the information write in the file.....
file=open("mca_niet.txt",'w')           #it creates a new file in the foldar...
# print(file)
file.write("Python\n")           #It write the new text in the file and erase the prev. information...
file.write("Noida")
file.close()
'''
#we can only aplli "write" method on it...



#we add the information in the file.....
'''
file=open("mca_niet.txt",'w')           #it creates a new file in the foldar...
# print(file)
file.write("Python\n")           #It write the new text in the file and erase the prev. information...
file.write("Noida")
file.writelines("NIET\nBYE BYE\nMOYE MOYE...!\n")
file.writelines(["NIET\nBYE BYE\nMOYE MOYE...!"])

file.close()
'''

########==========================================================================#############
#              # (iii). Append #      #
'''
file=open("mca_niet.txt",'a')
file.write("\nThis information is appended into the file.\n")
file.writelines(["NIET\n","Delhi\n"])
file.close()
'''


#======================================================================================

#EX.
#using while loop:-
'''
file=open("mca_niet.txt",'r')
line=file.readline()
while(line):
    print(line)
    line=file.readline()
file.close()
'''

#EX.
### using for loop:-
'''
file=open("mca_niet.txt",'r')
line=file.readline()
for i in(line):
    print(line)
    line=file.readline()
file.close()
'''
#EX. by sir
#using for loop:-  "short mathod"
'''
file=open("mca_niet.txt",'r')
for line in file.readlines():
    print(line)
'''


#EX.
#print first word by letter by letter using for loop:-
'''
file=open("mca_niet.txt",'r')

for line in file.readline():
    print(line)
'''

#EX.
#print first word by letter by letter using for loop:-
'''
file=open("mca_niet.txt",'r')

for i in file.readline():
    print(i)
file.close()
'''


#EX.
#print word by word
'''
file=open("mca_niet.txt",'r')

for line in file.readlines():
    print(line)
    for word in line.split():
        print(word)
file.close()
'''
#===================================================================================
##################################################################################
##############
##########
######
#
##################################
#=====
#====================================================================================

#       # directaries #       #


#EX.
'''
import os
#print(os.__dir__())

        
# os.mkdir('new directory')  #create a new directory named 'new directory'
#print(os.getcwd())
print(os.stat("NIET"))
'''



#===================================================================
#       # Exception #       #
#exception is a type of ERROR can be handled by the following certain steps.
#EX.

# 1* file not found error
# 2* key error
# 3* index error
# 4* type error


'''
a=50
try:
    b = int(input())
    print(a/b)
except ZeroDivisionError as e:
    print(e)
    print("please enter valid input")
except ValueError as v:
    print(v)
    print("please enter proper input")
finally:
    print("Statements after division")
    print("end of the program")

'''

# Raise :--> gave forcefully error

a=50
try:
    b = int(input())
    print(a/b)
except ZeroDivisionError as e:
    print(e)
    print("please enter valid input")
except ValueError as v:
    print(v)
    print("please enter proper input")
finally:
    print("Statements after division")
    print("end of the program")

raise ValueError()     #it gave forcefully ERROR


    
















