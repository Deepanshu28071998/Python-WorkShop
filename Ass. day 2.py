
     


#Q1).
'''
a = int(input("Enter the number: "))
if (a%3==0):
    if (a%7==0):



        print("Our Fav.")
    else:
        print("Sir Fav.")
elif (a%7==0):
    print("My fav.")
else:
    print("Not Fav.")
'''
#Q2).
'''
alp=str(input("Enter a Alphabet: "))
if alp=='a':
    print("'a' is a vowel.")
elif alp=='e':
    print("'e' is a vowel.")
elif alp=='i':
    print("'i' is a vowel.")
elif alp=='o':
    print("'o' is a vowel.")
elif alp=='u':
    print("'u' is a vowel.")
else:
    print(alp," is not a vowel.")
'''
#Q3).
'''

    
def is_leap(year):
    """
    Check if the given year is a leap year or not.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
is_leap(int(input("Enter the year: ")))    
'''
##
'''
while True:
    def is_leap(year):
    
    #Check if the given year is a leap year or not.
    
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f"{year} is a leap year")
                else:
                    print(f"{year} is not a leap year")
            else:
                print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    is_leap(int(input("Enter the year: ")))    

'''
#Q4).
'''
def marks(mark):
        per=(mark/50)*100
        if per>=90:
            print("Grade 'A'")
        elif per>=80:
            print("Grade 'B'")
        elif per>=70:
            print("Grade 'C'")
        elif per>=60:
            print("Grade 'D'")
        elif per>=40:
            print("Grade 'E'")
        else:
            print("Grade 'F'")

while True:
    print("1. Physics, \n2. Chemistry, \n3. Biology, \n4.Mathematics, \n5. Computer \n0. Exit")
    sub=int(input())
    if sub==0:
        break
    elif sub==1:
        marks(float(input("Marks on Physics: ")))
    elif sub==2:
        marks(float(input("Marks on Chemistry: ")))
    elif sub==3:
        marks(float(input("Marks on Biology: ")))
    elif sub==4:
        marks(float(input("Marks on Mathematics: ")))
    elif sub==5:
        marks(float(input("Marks on Computer: ")))
    else:
        print("Invalid option")
'''
    
#Q5.
'''
basic_salary=int(input("Enter your base salary: "))
    
if basic_salary<=10000:
    hra=((basic_salary*20)/100)
    da=((basic_salary*80)/100)
elif basic_salary<=20000:
    hra=((basic_salary*25)/100)
    da=((basic_salary*90)/100)
else:
        
    hra=((basic_salary*30)/100)
    da=((basic_salary*95)/100)
new_b_s= basic_salary+hra+da
print("The Base Salary is ",basic_salary,"\nThe HRA is ",hra,"\nThe DA iS ",da,"\nThe New Salary is ",new_b_s)
print("Thank You")
'''



##
'''
while True:
    name=str(input("Enter the name of the employ:"))
    basic_salary=int(input("Enter your base salary: "))
    #hra%=float(input("Enter the HRA %: "))
    #da%=float(input("Enter the DA %: "))
    if basic_salary<=10000:
        hra=((basic_salary*20)/100)
        da=((basic_salary*80)/100)
    elif basic_salary<=20000:
        hra=((basic_salary*25)/100)
        da=((basic_salary*90)/100)
    else:
        
        hra=((basic_salary*30)/100)
        da=((basic_salary*95)/100)
    new_b_s= basic_salary+hra+da
    print("The Base Salary is ",basic_salary,"\nThe HRA is ",hra,"\nThe DA iS ",da,"\nThe New Salary is ",new_b_s)
    print("Thank You")
'''
