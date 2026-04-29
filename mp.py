#store a 4 digit PIN number
pin = "1234"
#ask user to enter their PIN number
user_pin = input("Please enter your 4-digit PIN number: ")
#check if the entered PIN number is correct
if user_pin == pin:
    print("PIN accepted. Access granted.")
else:    print("Incorrect PIN. Access denied.")
#if user enters wrong PIN, ask them to try again upto 2 times where after 3 failed attempts, lock the account
 
for attempt in range(4):
    user_pin = input("Please enter your 4-digit PIN number: ")
    if user_pin == pin:
        print("PIN accepted. Access granted.")
        break 

    if user_pin != pin:
        print("Incorrect PIN. Please try again.")
        break 
    else: user_pin != pin
    print("Account locked due to too many failed attempts. Please contact customer support.")   
    
     
    

