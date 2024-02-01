import operator
sid=['0231mca001','0231mca002','0231mca003','0231mca004','0231mca005','0231mca006','0231mca007','0231mca008','0231mca009','0231mca010','0231mca011','0231mca012','0231mca015']
dic={"A":0,"B":0,"C":0,"D":0,"E":0}
suma=0
sumb=0
sumc=0
sumd=0
sume=0

while True:
    erp=input("Enter your ERP ID: ")
    if erp in sid:
        print ('Choice your option:\n(1). "A"\n(2). "B"\n(3). "C"\n(4). "D"\n(5). "E"\n(0). "EXIT"')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            suma += 1
            dic["A"]=suma
            


        elif choice == 2:
            sumb+=1
            dic["B"]=sumb
        
        elif choice == 3:
            sumc+=1
            dic["C"]=sumc
        
        elif choice == 4:
            sumd+=1
            dic["D"]=sumd

        elif choice==5:
            sume+=1
            dic["E"]=sume
        
        elif choice==0:
            print("Result is:")
            print("A",dic["A"])
            print("B",dic["B"])
            print("C",dic["C"])
            print("D",dic["D"])
            print("E",dic["E"])

            max_value = max(dic.values())
            print("The winner of this elections are:",max_value,":",list(dic.keys())[list(dic.values()).index(max_value)])
            break

            
        else:
            print("Invalid choice.")
            
    else:
        print ("ERP ID not found")
# print("Result is:")
# print(dic["A"])
# print(dic["B"])
# print(dic["C"])
# print(dic["D"])
# print(dic["E"])

# max_value = max(operator.itemgetter(1), dic.items())
# print("The winner of this elections are:",max_value)
