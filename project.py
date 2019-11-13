authorize_personnel_list = []
authorize_personnel_list.append("quanfeiy")
authorize_personnel_list.append("zoujinto")

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
            answer = input("Access deny, you are not authorized to use this system.")        
            verification = "false"
            from playsound import playsound
            playsound('fbi-open-up-sfx.mp3')            
    
if verification == "true":
    answer = input("What would you like to do? Enter read or write: ")
    if answer == "read":
        my_file = open("project_test.txt", "r") 
        for line in my_file:
            print(line)
    
    