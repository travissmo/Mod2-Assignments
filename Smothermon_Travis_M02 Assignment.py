#Travis Smothermon
#Smothermon_Travis_M02Assignment.py
#This program takes your name and your GPA and tells you if you made the Deans List and/or the Honor Roll
last_name= input(str("Enter your last name or enter ZZZ to quit "))
if last_name != "ZZZ":
    first_name = input(str("Enter your first name "))
    GPA_input = float(input("Enter your GPA "))

    
    if GPA_input >= 3.25:
        print("Congrats you made the Honor Roll! ")
        if GPA_input >= 3.5:
            print("Congrats you made the Deans List! ")
    else:
        print("Sorry, you did not make the Honor Roll or the Deans List ")




