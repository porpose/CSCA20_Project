#This is the security module in the project, you have three chance to enter
#the correct password, otherwise the program will lock and trigger the alarm.
import csv
from playsound import playsound

authorize_personnel_list = []
authorize_personnel_list.append("quanfeiy")
authorize_personnel_list.append("zoujinto")
enter_valid = "true"
verification = "false"
answer = input("Welcome to criminal risk control system, please enter your id: ")

while answer == "":
    enter_valid == "false"
    print("You are not allow to enter empty id, please try again")
    answer = input("Welcome to criminal risk control system, please enter your id: ")
if answer == authorize_personnel_list[0] or answer == authorize_personnel_list[1]:
        print("Access verifcation completed, hello "+ str(answer))
        verification = "true"
else:
    answer = input("Access deny, you have 2 more chances. Enter your id: ")
    if answer == authorize_personnel_list[0] or answer == authorize_personnel_list[1]:
            print("Access verifcation completed, hello "+ str(answer))
            verification = "true"        
    else:
        answer = input("Access deny, you have 1 more chance. Enter your id: ")    
        if answer == authorize_personnel_list[0] or answer == authorize_personnel_list[1]:
            print("Access verifcation completed, hello "+ str(answer))
            verification = "true"
        else: 
            print("Access deny, you are not authorized to use this system.")
            verification = "false"
            while verification == "false":
                playsound('fbi-open-up-sfx.mp3')
                               
    
 #This is the search module in the project   
if str(verification) == "true":
    answer = input("What would you like to do? Enter read or write or search or add or remove: ")
    if answer == "read":
        my_file = open("crime_record_list.csv", "r")
        my_file = csv.reader(my_file)
        data = list(my_file)
        print(data[0], data[1:])
    
        '''(str,str) -> list
        REQ:When enter the firstname and the last name it should pull up the
        the criminal's record
        >>>Enter the first name:Ben
        >>>Enter the last name:Swager
           ['Ben', 'Swager', 'M', '5/3/1972', 'Armed robbery', '2/3/1993']
        '''
        #Enter the firstname
        #Enter the lastname
        #put the first and lastname together as a variable to enable the search
        #Loop through the file to find the record base on the name
        #loop through the file from the first record to the end
        #once find out the name, we print out the record
    if answer == "search":
        my_file = open("crime_record_list.csv", "r")
        my_file = csv.reader(my_file)
        data = list(my_file)
        criminal_id = input("please enter the criminal id: ")
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
    print("Record successfully added!")

exit = input("Press Enter to exit...")   
