#user enters amount they would like to send
print("Welcome to the Mpesa service! I am your virtual assistant. What would you like to do today?")
amount = input("Please enter the amount you would like to send: ")
recipient = input("Please enter the recipient's phone number: ")
if int(amount) < 0:
    print("Invalid amount. Please enter a positive number.")
else:
    print("Amount successfully sent.")



    
