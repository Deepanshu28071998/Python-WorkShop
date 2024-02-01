n=int(input("Enter the number of elements in your list: "))
l=[]
for i in range(n):
    e=int(input("Enter number {}: ".format(i+1)))
    l.append(e)
print(l)
print("Sum of all elements in your list  is: ",sum(l))
print("first element of the list is:",l[0])
print("Last element of the list is:",l[i])
print("Avrage of the list is:",(sum(l)/n))
a=int(input("Gave the value which is find in the list: "))
while a in l:
    for i in l:
        
        if i==a:
            print(a,"is in the list")

else:
    print(a,"is not in the list")

