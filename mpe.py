#vehicle fare counter for total passengers
#vehicle starts with 0 shillings therefore no passengers at the beginning
print("Welcome to the Vehicle Fare Counter! I am your virtual assistant. Let's calculate the total fare for your passengers.")
#input the amount paid by the passenger
amount_paid = int(input("Please enter the amount paid by the passenger: "))
#transformations
if amount_paid >= 50:
    print("Passenger has paid the fare. Access granted.")
elif amount_paid < 50:
    print("Passenger has been flagged!!!!!!!!!!!!! Access denied.")
#add a loop to allow multiple passengers to pay their fare and calculate the total fare collected at the end of the day
total_fare = 0
amount_paid = int(input("Please enter the amount paid by the passenger: "))
total_amount = 0
while amount_paid >= 0:
    if amount_paid >= 50:
        print("Passenger has paid the fare. Access granted.")
        total_amount= total_amount + amount_paid
        print("Total fare collected so far: ", total_amount)
        total_fare += amount_paid
    elif amount_paid < 50:
        print("Passenger has been flagged!!!!!!!!!!!!! Access denied.")
    amount_paid = int(input("Please enter the amount paid by the passenger: "))
