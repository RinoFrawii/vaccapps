# *********************************************************
# Program: VaccApps.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL1V-TL4V
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211103423 | MUHAMMAD RINO FRAWIDYA BIN SUHERI | 1211103423@student.mmu.edu.my | 01123368808
# Member_2: 1211102590 | NUR HANISAH BINTI MOHD PAUZI | 1211102590@student.mmu.edu.my | 0177922679
# Member_3: 1211102895 | MUHAMMAD IRFAN BIN MOHD NAZRI| 1211102895@student.mmu.edu.my | 0199244016
# Member_4: 1211102693 | HARANIYA A/P KANAPARAN | 1211102693@student.mmu.edu.my | 0168512248
# *********************************************************
# Task Distribution
# Member_1:PUBLIC USER
# Member_2:ADMIN
# Member_3:REPORT AND FLOWCHART
# Member_4:LOGIN AND REGISTER
# *********************************************************


#THIS SECTION IS FOR THE MENU AND RESULT DISPLAY IN THE VACCINATION APPS

#SHOWS FIRST INTERFACE WHEN THE APPS IS USED
def main():
    print("-"*31)
    print("WELCOME TO THE VACCINATION APPS")
    print("-"*31)
    print()
    print("1 - Register")
    print("2 - Login")
    print("3 - Admin Login")
    print()
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2','3']:
            break
    if userChoice == '1':
        Register()
    elif userChoice == '2':
         Login()
    else:
        adminLogin()

#USER REGISTRATIONS
def Register():
    print("--------")
    print("REGISTER")
    print("--------")
    print()
    while True:
          userName = input("Enter Your Name: ").title()
          if userName != '':
            break
    userName = sanitizeName(userName)
     
    while True:
          userPassword = input("Enter Your Password: ")
          if userPassword != '':
               break 

    while True:
         confirmPassword = input("Confirm Your Password: ")
         if confirmPassword == userPassword:
           break
         else:
           print("Passwords Don't Match")
           print() 

    while True:
         phoneNumber = input("Enter Your Phone No.: ")
         if phoneNumber != '':
           break
    while True:
         Age = input('Enter Your Age: ')
         if Age != '':
           break
    while True:
         postCode = input("Enter Your Postcode: ")
         if postCode != '':
           break

    addUserInfo([userName,userPassword,phoneNumber,Age,postCode])
    UserNamePass([userName,userPassword])

    while True:
         print()
         done = input("Your Registration Is Done!\nPress (L) To Login:\nPress (B) To Go Back To Main Menu:").lower()
         if done == 'l':
              Login()
              break
         elif done == 'b':
              main()
              break        

#USER LOGIN DISPLAY
def Login():
     print('-'*5)
     print("LOGIN")
     print('-'*5)
     print()
     usersInfo = {}
     with open('namepass.txt','r') as file:
          for line in file:
               line = line.split()
               usersInfo.update({line[0]: line[0]})
               

     while True:
          userName = input("Enter Your Name: ").title()
          userName = sanitizeName(userName)
          if userName not in usersInfo:
               print("You Are Not Registered")
               main()
          else:
               break
     while True:
          userPassword = input("Enter Your Password: ")
          if UserNamePass([userName,userPassword]):
               print("Incorrect Password")
               print()
          else:
               print("Logged in")
               print()
               pubUser()
               break

#ADMIN LOGIN DISPLAY              
def adminLogin():
     print('-'*5)
     print("ADMIN LOGIN")
     print('-'*5)
     print()
     usersInfo = {}
     with open('nameadmin.txt','r') as file:
          for line in file:
               line = line.split()
               usersInfo.update({line[0]: line[1]})
               

     while True:
          userName = input("Enter Admin Name: ").title()
          userName = sanitizeName(userName)
          if userName not in usersInfo:
               print("You Are Not Registered")
               main()
          else:
               break
     while True:
          userPassword = input("Enter Admin Password: ")
          if UserNamePass([userName,userPassword]):
               print("Incorrect Password")
               print()
          else:
               print()
               print("Logged In!")
          pubAdmin()

#USER MAIN MENU DISPLAY
def pubUser():
    print('-'*9)
    print('MAIN MENU')
    print('-'*9)
    print()
    print('1 - Update Your Information')
    print('2 - Check Your Appointment')
    print('3 - Confirm your appointment')
    print('4 - Logout')
    print()
    while True: 
        print()
        userOption = input('Choose an option: ')
        if userOption in ['1','2','3','4']:
            break
    if userOption == '1':
        updateInfo()
    elif userOption == '2':
        checkAppoint()
    elif userOption == '3':
        confAppoint()
    else:
        main()

#USER UPDATE THEIR MEDICAL INFO
#USER AUTO ASSSIGN THEIR APPOINTMENT
def updateInfo():
     print('-'*30)
     print("Answer All The Questions Below")
     print('-'*30)
     print('y for yes \nn for no')
     while True:
          username = input('Enter Your Name: ').title()
          if username != '':
               break
     username =sanitizeName(username)

     while True:
          occu = input('Enter Your Occupation: ').title()
          if occu != '':
               break

     while True:
          q1 = input('Have you had close contact with a covid positive patient?\n').lower()
          if q1 in ['y','n']:
               break
          elif q1 != '':
               break

     while True:
          q2 = input('Have you ever been to any event/areas associated with known COVID-19 cluster?\n').lower()
          if q2 in ['y','n']:
               break
          elif q2 != '':
               break
          
     while True:
          q3 = input('Have you had any COVID-19 symptoms?\n').lower()
          if q3 in ['y','n']:
               break
          elif q3 != '':
               break

     while True:
          q4 = input('Do you work as a frontliner?\n').lower()
          if q4 in ['y','n']:
               break
          elif q3 != '':
               break

     addUserMedInfo([username,occu,q1,q2,q3])
     
     while True:
          rsvp = [q1,q2,q3,q4]
          if 'y' in rsvp:
                    print("Please quarantine yourself for 14 days and take a swab test")
                    print("If you are a frontliner, please make sure that you are free from COVID-19")
                    highRisk([username,occu,q1,q2,q3,q4])

                    break
          else:
                    print('You are ready for vaccination')
                    lowRisk([username,occu,q1,q2,q3])

                    date = input('Choose Your Appointment Date (YYYY-MM-DD): ')
                    import random #USE RANDOM MODULE

                    time = ['0900','1000','1100','1200','1300','1400','1500','1600']
                    randtime=(random.choice(time))


                    with open("vaccenter.txt", "r") as f:
                          lines = f.readlines()
                          randcenter=(random.choice(lines))
                    
                    vaccList([username,date,randtime,randcenter])

                    break
                    
     while True:
         print()
         done = input("Press (B) to go back to the main menu \nPress (C) to check your appointment\n").lower()
         if done == 'b':
              pubUser()
              break
         elif done == 'c':
              checkAppoint()
              break

#ADMIN MAIN MENU DISPLAY
def pubAdmin():
     print()
     print("1 - View all user")
     print("2 - Vaccination Center")
     print("3 - Assign Appointment")
     print("4 - Users Medical Info")
     print("5 - Back To Main Menu")
     while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2','3','4','5']:
            break
     if userChoice == '1':
        viewUser()
     elif userChoice == '2':
        vaccenter()
     elif userChoice == '3':
        assignAppoint()
     elif userChoice == '4':
        userMedInfo()
     elif userChoice == '5':
        main()

#VACCINATION CENTER MENU DISPLAY         
def vaccenter():
    print('-'*18)
    print("Vaccination Center")
    print('-'*18)
    print()
    print("1 - View Vaccination Center")
    print("2 - Add Vaccination Center")
    while True:
         print()
         userChoice = input("Choose An Option: ")
         if userChoice in ['1', '2']:
              break
    if userChoice == '1':
        viewVacc()
    elif userChoice == '2':
        addVacc()  

#ADMIN ADD NEW VACCINATION CENTER      
def addVacc():
    print('-'*26)
    print("Add New Vaccination Center")
    print('-'*26)

    while True:
       vaccenter = input('Vaccination Center Name: ')
       if vaccenter != '':
             break

    while True:
         state = input('State Of Vaccination Center: ')
         if state != '':
             break 

    while True:
         capacity = input('Capacity of The Vaccination Center: ')
         if capacity != '':
          break

    vacCenter([vaccenter,state,capacity])
   

#USER MEDICAL INFORMATION AND RECORDS MENU DISPLAY
def userMedInfo():
     print('-'*19)
     print('User Medical Record')
     print('-'*19)
     print()
     print('1 - All Users Medical Info ')
     print('2 - High Risk Users ')
     print('3 - Low Risk Users ')
     while True:
          print()
          userChoice = input('Choose An Option: ')
          if userChoice in ['1','2','3']:
               break
     if userChoice == '1':
          viewMed()
     elif userChoice == '2':
          viewHighRisk()
     elif userChoice == '3':
          viewLowRisk()

#ADMIN MANUALLY ASSSIGN APPOINTMENT FOR USERS    
def assignAppoint():
    print("--------")
    print("Set User's Appointment")
    print("--------")
    print()
    while True:
          userName = input("Enter User's Name: ").title()
          if userName != '':
            break
    userName = sanitizeName(userName)
     
    while True:
          userLocation = input("Enter User's Vaccination Center: ")
          if userLocation != '':
               break 

    while True:
         userDate = input("Enter User's Vaccination Date [YYYY-MM-DD]: ")
         if userDate != '':
           break

    while True:
         userTime = input("Enter User's Vaccination Time [e.g. 1300]: ")
         if userTime != '':
           break

    vaccList([userName,userDate,userTime,userLocation])
    pubAdmin()

#USER CONFIRM THEIR APPOINTMENT
def confAppoint():
     print('-'*30)
     print("Kindly confirm your appointment:")
     print('-'*30)
     print('y for Yes and n for No')
     confirmAppoint = input("Choose An Option: ")
     if confirmAppoint == 'y':
        print()
        print("Your appointment has been confirmed.")
     elif confirmAppoint == 'n':
        print()
        print("You have cancelled your appointment. Kindly re-scheduled.")
     pubUser()

def quit():
    exit()

#THIS SECTION IS FOR FUNCTION FOR STORING ALL THE DATA IN THE APPS
#ALL CODE BELOW USED FOR APPEND AND READ ALL THE DATA IN THE TEXT FILES

#ADD USER INFO
def addUserInfo(userInfo: list):
     with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(',')
        file.write('\n')

#USER LOGIN HISTORY
def UserNamePass(userInfo: list):
      with open('namepass.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')

#SPLIT USERNAME THAT HAVE MORE THAN ONE WORD WITH (-)         
def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName

#FOR ADMIN TO VIEW ALL REGISTERED USERS
def viewUser():
     with open('userInfo.txt','r') as file:
          contents = file.read()
     print()
     print('------------------------View All User------------------------')   
     print()       
     print(contents)
     print('-'*61)
     pubAdmin()

#FOR ADMIN TO VIEW ALL REGISTERED VACCINATION CENTER
def viewVacc():
     with open('vaccenter.txt', 'r') as file:
          contents = file.read() 
     print()
     print('-------------------View Vaccination Center------------------')
     print()
     print(contents)
     print('------------------------------------------------------------')

#FOR USER TO CHECK THEIR APPOINTMENT BY INSERTING THEIR NAME KEYWORD
def checkAppoint():
     name = input('Enter Your Name To Check Your Appointment: ')
     with open("vaccList.txt") as openfile:
          for line in openfile:
                if name in line.lower():
                     print()
                     print("----------------Your Vaccine Appointment----------------")
                     print()
                     print(line)
                     print("--------------------------------------------------------")
                     pubUser()

#ADD USER MEDICAL INFO AND CATEGORIZE THEM TO HIGH RISK AND LOW RISK
def addUserMedInfo(userInfo: list):
     with open('medinfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(',')
        file.write('\n')

#FOR ADMIN TO VIEW ALL USER MEDICAL INFO
def viewMed():
     with open('medinfo.txt', 'r') as file:
          contents = file.read() 
     print()
     print('------------------------Medical Records----------------------')
     print()
     print(contents)
     print('-'*61)
     pubAdmin()

#FOR ADMIN TO ADD NEW VACCINATION CENTER
def vacCenter(userInfo: list):
     with open('vaccenter.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(',')
        file.write('\n')

#STORE HIGH RISK USER'S MEDICAL INFORMATION
def highRisk(userInfo: list):
     with open('highrisk.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(',')
        file.write('\n')

#FOR ADMIN TO VIEW HIGH RISK USER
def viewHighRisk():
     with open('highrisk.txt', 'r') as file:
          contents = file.read() 
     print()
     print('-----------------------High Risk Users--------------------')
     print()
     print(contents)
     print('-'*59)
     pubAdmin()

#STORE LOW RISK USER'S MEDICAL INFORMATION
def lowRisk(userInfo: list):
     with open('lowrisk.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(',')
        file.write('\n')

#FOR ADMIN TO VIEW ALL LOW RISK USER
def viewLowRisk():
     with open('lowrisk.txt', 'r') as file:
          contents = file.read() 
     print()
     print('-----------------------Low Risk Users----------------------')
     print()
     print(contents)
     print('-'*61)
     pubAdmin()

#STORE ALL USER APPOINTMENT INFORMATIONS INCLUDING NAME,DATE,TIME AND VACCINATION CENTER
def vaccList(userInfo: list):
     with open('vaccList.txt', 'a') as file:
         for info in userInfo:
            file.write(info)
            file.write(',')
         file.write('\n')

main()