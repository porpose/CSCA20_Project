#This is the security module in the project, you have three chances to enter
#the correct password, otherwise the program will lock and trigger the alarm.
import csv
from playsound import playsound

authorize_personnel_list = []
authorize_personnel_list.append("quanfeiy")
authorize_personnel_list.append("zoujinto")
enter_valid = "true"
verification = "false"
answer = input("Welcome to the Criminal Record System, please enter your ID: ")
#This program does not allow the user to enter empty id. If user don't enter the
#password it won't exit the while loop so that it will keep requesting ID entry
while answer == "":
    answer = input("You are not allow to enter empty id, please try again: ")
if answer == authorize_personnel_list[0] or answer == authorize_personnel_list[1]:
        print("Access verifcation completed, hello " + answer + "!")
        verification = "true"
else:
    answer = input("Access deny, you have 2 more chances. Enter your id: ")
    if answer == authorize_personnel_list[0] or answer == authorize_personnel_list[1]:
            print("Access verifcation completed, hello " + answer + "!")
            verification = "true"        
    else:
        answer = input("Access deny, you have 1 more chance. Enter your id: ")    
        if answer == authorize_personnel_list[0] or answer == authorize_personnel_list[1]:
            print("Access verifcation completed, hello " + answer + "!")
            verification = "true"
        else: 
            print("Access deny, you are not authorized to use this system.")
            verification = "false"
            while verification == "false":
                playsound('fbi-open-up-sfx.mp3')
    
#This is the read-write to file module in the project only runs when verification
#is true
'''(str) -> str(list)
When people try to read all the data base they can choose to enter read to pull
out all the information
>>>What would you like to do? Enter read or update or search or add or remove: 
>>>['id', 'First name', 'Last name', 'gender', 'date of birth', 'crime title', 'incident date'] 
[['1', 'Ben', 'Swager', 'M', '1972-05-03', 'Armed robbery', '1993-02-03'], 
['2', 'Yaser', 'Abu', 'M', '1957-01-27', 'Murder', '2008-01-01'], 
['3', 'Alexis', 'Flore', 'M', '1982-01-17', 'Kidnap murder', '2000-07-31'], 
['4', 'Arnoldo', 'Jimenez', 'M', '1982-02-19', 'murder', '2012-05-17']]
'''
if verification == "true":
    #This part is asking what kind of task that the user try to do base on entry
    #user can choose read, update, search, add, or remove.
    answer = input("What would you like to do? Enter read or update or search or add or remove: ")
    if answer == "read":
        #when user enter the string read they can choose to read thorugh all the
        #record. 
        my_file = open("crime_record_list.csv", "r")
        my_file = csv.reader(my_file)
        data = list(my_file)
        print(data[0], data[1:])
    
    #Description for the search module starts here
        '''(str,str) -> list
        REQ:When enter the criminal ID it should pull up the
        the specific criminal's record
        >>>Please enter the Criminal ID:1
        >>>['id', 'First name', 'Last name', 'gender', 'date of birth', 'crime title', 'incident date']['Ben', 'Swager', 'M', '5/3/1972', 'Armed robbery', '2/3/1993']
        '''

    if answer == "search":
        my_file = open("crime_record_list.csv", "r")
        my_file = csv.reader(my_file)
        data = list(my_file)
        criminal_id = input("Please enter the criminal id: ")
        print(data[0],data[int(criminal_id)])        

    if answer == "add":
    
        '''(str,str,str,str,str,str,str) -> Nonetype
        Base on the entry, add new crime record to the file.
        >>>Please enter ID: 5
        >>>Please enter First name: Ken
        >>>Please enter Last name: Zolberg
        >>>Please enter gender: M
        >>>Please enter the date of birth(yyyy-mm-dd): 2000-01-01
        >>>Please enter crime_title: kidnap
        >>>Please enter incident date: 2000-01-02
        '''
        ID = ""
        First_name = ""
        Last_name = ""
        gender = ""
        date_of_birth = ""
        crime_title = ""
        incident_date = ""
        #This program doesn't allow any catagory left blank information, if any
        #information is blank it will require the user to re-enter everything
        #until all the categories are correctly filled
        while ID == "" or First_name == "" or Last_name == "" or gender == "" or date_of_birth == "" or crime_title == "" or incident_date == "":
            ID = input("Please enter ID: ")
            First_name = input("Please enter First name: ")
            Last_name = input("Please enter Last name: ")
            gender = input("Please enter the gender(M/F): ")
            date_of_birth = input("Please enter the date of birth(yyyy-mm-dd): ")
            crime_title = input("Please enter the crime title: ")
            incident_date = input("Please enter the incident date(yyyy-mm-dd): ")
        crime_record = [ID, First_name, Last_name, gender, date_of_birth, crime_title, incident_date]
        with open("crime_record_list.csv", "a") as fd:
            wr = csv.writer(fd, dialect='excel')
            wr.writerow(crime_record)
        print("Record added successfully!")
        #when entry for task is "update", the update information module is launched
    if answer == "update":
        '''>>>Please enter the criminal id: 4
        ['id', 'First name', 'Last name', 'gender', 'date of birth', 'crime title', 'incident date'] ['4', 'Arnoldo', 'Jimenez', 'M', '2/19/1982', 'murder', '5/17/2012']
           >>>What do you want to change?: gender
           >>>What do you want this item be changed to?: F
           Record updated successfully!
           Press Enter to exit...
        '''
        my_file = open("crime_record_list.csv", "r")
        my_file = csv.reader(my_file)
        data = list(my_file)
        criminal_id = input("Please enter the criminal id: ")
        print(data[0],data[int(criminal_id)]) 
        #Upper part is for user to double check if this is the record they
        #want to revise
        #Select the item you want to change by type in the variable's name
        answer1 = input("What do you want to change? Type First name, Last name, gender, date of birth, crime titile or incident date (space included): ")
        answer2 = input("What do you want this item be changed to?: ")
        index = data[0].index(answer1)
        data[int(criminal_id)][index] = answer2
        with open('crime_record_list.csv', 'w', newline="") as writer_file:
            writer = csv.writer(writer_file)
            writer.writerows(data)        
        writer_file.close()        
        print("Record updated successfully!")
        #when task entry is "remove" the remove record module is launched.
        #It also provides a chance for user to double check if the record
        #pull out based on the ID is the one they want to remove from the system.
    if answer == "remove":
        my_file = open("crime_record_list.csv", "r")
        my_file = csv.reader(my_file)
        data = list(my_file)                     
        ID = input("Which record do you want to remove? Enter the criminal id: ")
        print(data[0],data[int(ID)])
        data.pop(int(ID))
        with open('crime_record_list.csv', 'w', newline="") as writer_file:
            writer = csv.writer(writer_file)
            writer.writerows(data)        
        writer_file.close()        
        print("Record removed successfully!")         

#When your task is done, press enter to exit the program.
exit = input("Press Enter to exit...")   
