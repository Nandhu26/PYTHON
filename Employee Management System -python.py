#Employee Management System in Python for getting and the credentials of the employees
#Author : Nandhana
#Created Date: 16-Aug-2021
#Modified on: 17/08/2021 6:00 p.m.
#Modified by: Nandhana 

import re
import datetime

def isrepeated(ename):
    for i in range (0,len(ename)-2):
           if ename[i]==ename[i+1] and ename[i+1]==ename[i+2]:
               return True
    return False

def findage(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    

def validateemployeeID():
    while True:
        ID=input('Enter your Employee ID:')
        EmpID= 'ACE'+ID
        if (not(ID.isdigit())):
            print('ID should be numeric."Eg:0001".')
            continue
        elif int(ID)==0:
            print('ID should not be null."Eg:0001".')
            continue
        elif len(ID)!=4:
            print('Id should be in 4 digits-"Eg:0001"')
            continue
        else:
            return EmpID

def validateemployeename():
    while True:
        employeenames=input("Enter your Name:")
        if (not(employeenames.isalpha())):
            print('Name should be in alphabets.Please try again - "Eg:Ram"')
            continue
        elif len(employeenames)<=3:
            print('Name should have atlease 3 letters.Please try again - "Eg:Ram"')
            continue            
        elif isrepeated(employeenames):
            print('The Name you entered has repeated alphabets. Please enter a valid Name - "Eg:Ram"')
            continue
        elif ' ' in employeenames:
            print('Please enter name without space - "Eg:Ram"')
            continue
        else:
            return employeenames

def validatedateofbirth():
    while True:
        try:
            dob1=input('Enter your dateofbirths in this format DD-MM-YYYY "Eg:26-08-1999" :')
            dob= datetime.datetime.strptime(dob1, '%d-%m-%Y')
            age=findage(dob)
            if age<0:
                print("The date doesnt exist.Please try again.")
            elif age<18 and age>=0:
                print('Please try again after 18.All the best')
            elif age>60:
                print("It was a pleasure working with you.Happy retired life !")
            else:
                return age,dob1
        except:
            print("Invalid Date.Please try again.Eg:26-08-1999 :")
            continue
        
            
def validatedateofjoining():
    while True:
        try:
            joindate1=input('Enter your joiningdate in the format DD-MM-YYYY- "Eg:26-08-1999 ":')
            joindate= datetime.datetime.strptime(joindate1, '%d-%m-%Y')
            experience=findage(joindate)
            if experience<0:
                print("Invalid date.Enter again")
            else:
                return str(experience),joindate1
        except:
            print("Invalid date.Please try again Eg:26-08-1999 : ")
            continue  
def validatequalifications():
    while True:
        try:
            print ("\nQualifications : \n1)B.E ECE \n2)B.E EEE \n3)B.E CSE  \n4)B.TECH IT\n5)OTHERS ")
            option = int(input("\nSelect your qualification-(1 to 5): "))

            if option == 1:
                qualification = " B.E ECE"
                return qualification
            elif option == 2:
                qualification = "B.E EEE "
                return qualification
                
            elif option == 3:
                qualification = "B.E CSE "
                return qualification

                
            elif option == 4:
                qualification ="B.TECH IT "
                return qualification
               
            elif option == 5:
                qualification=str(input('Enter your Qualification '))
                return qualification
            else:
                print("Please enter a Valid Option")
                continue
        except:
                print("Invalid option. Select your Options-(1 to 5): ")
                continue


def validateemail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'
    while True:
     
        email=input('Enter your Email ID:Eg-abc@gmail.com :')
        if(re.fullmatch(regex, email)):
            return email
            
        else:
            print("Please enter a valid email ID - Eg-abc@gmail.com")
            continue
 
def validatemobilenumber():
    while True:
        mobileno=input('Enter your Mobile Number:') 
        if (not(mobileno.isdigit())):
            print(' Mobile number should be numeric.Please try again')
            continue
        elif len(mobileno)!=10:
            print('Please enter 10 digit phone number')
            continue
        elif mobileno.startswith(('0' , '1' , '2', '3', '4', '5')):
            print('Please enter phone number starting with 6-10')
            continue
        else:
            return mobileno          


def validatesalary():
    while True:
        salary=input('Enter your salary:')
        
        if (not(salary.isdigit())):
            print('salary should be in numeric.Please try again')
            continue
        elif int(salary)==0:
             print('Salary should not be null.Please try again')
             continue
       
        elif int(salary)<1000 or int(salary) >10000000:
            print("salaryary range should be between 1000 and 1 crore. Please try again")
            continue
        else:
            return salary

def printinfo(eid,ename,eno,eemail,edob,ejoindate,equalification,esalary,eempdob,eempjoindate):
    print("\nEMPLOYEE DETAILS\n")
    print('Employee ID      : '+eid)
    print('Employee Name    : '+ename)
    print('Mobile Number    : '+ eno)
    print('Email ID         : '+eemail)
    print('Date of birth    : '+eempdob)
    print("Age              : you are {} years and We are happy to have you here".format(edob))
    print('Date of joining  : '+eempjoindate)
    print("experience       : "+ejoindate)
   
    print("Salary           : Rs."+esalary)
    print('Qualification    :  '+equalification)
    
if __name__ == '__main__':
    
    while True:
        print('\nWelcome to the Employee managament Portal.\nPlease enter your credentials\n')
        EMPLOYEEID=validateemployeeID()
        EMPLOYEENAME=validateemployeename()
        EMPLOYEENUMBER=validatemobilenumber()
        EMPLOYEEEMAIL=validateemail()
        EMPLOYEEAGE,EMPDOB=validatedateofbirth()
        EMPLOYEEEXPERIENCES,EMPLOYEEJOININGDATE=validatedateofjoining()
        EMPLOYEEQUALIFICATION=validatequalifications()
        EMPLOYEESALARY=validatesalary()
        printinfo(EMPLOYEEID,EMPLOYEENAME, EMPLOYEENUMBER,EMPLOYEEEMAIL,EMPLOYEEAGE,EMPLOYEEEXPERIENCES,EMPLOYEEQUALIFICATION,EMPLOYEESALARY,EMPDOB,EMPLOYEEJOININGDATE)
        final=input('\nDo you you want to enter another employee record?(Y/N)')
        if final=='Y':
            continue
        else:
            print('\nThank You\n')
            break