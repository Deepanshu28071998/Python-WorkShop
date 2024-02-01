#Ass.1
'''
start=int(input("Enter the starting range: "))
stop=int(input("Enter the stoping range: "))
esum=0
osum=0
print("Even Numbers.")
for i in range(start,stop+1):
    if (i%2==0):
        print(i,end= ' ')
        esum=esum+i
print("Sum of even numbers are: ",esum)
print("\nOdd numers")
for i in range(start,stop+1):
    if (i%2!=0):
        print(i,end=",")
        osum=osum+i
print("Sum of odd numbers are: ", osum)
'''
#Ass.2
#Problem
'''

a=int(input("Enter the value: "))
cnt=0
while a!=0:
    d=a%10
    if d!=0:
        cnt+=1
    a=a//10
print(cnt)

'''




#Ass. 3
