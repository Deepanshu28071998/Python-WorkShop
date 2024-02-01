#OUTPUT:-
'''
Enter the value in list1: m k t
Enter the value in list2: y i p
['m', 'k', 't']
['y', 'i', 'p']
['my', 'ki', 'tp']
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
