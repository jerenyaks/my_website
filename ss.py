def find_discount(price, member):
    if member:
        discount = price * 0.2
        print("Member discount:", discount)
    else:
        discount = price * 0.05
        print("Standard discount:", discount)
    return discount
    print("Discount applied.")
    return 0
    #The print statement and the second return statement will never be executed because they come after a return statement therefore they are impure
    #the return 0 is confusing especially when if/else run
    #the return is there to make the function impure because it will not execute the print statement and it will not display the discount applied and it will return 0 instead of the actual discount amount.
    #by putting the return statement before the print statement we have made the function impure because it will not execute the print statement and it will not display the discount applied and it will return 0 instead of the actual discount amount.
    #to make the function pure we should remove the return statement and the print statement and only return the discount amount without any side effects such as printing to the console.




def find_discount(price, member):
    """Return the discount amount — 20% of price for members, 5% for non-members."""
    if member:
        discount = price * 0.2
        print("Member discount:", discount)
    else:
        discount = price * 0.05
        print("Standard discount:", discount)
    return discount

find_discount(100, True)  # Output: Member discount: 20.0
find_discount(100, False) # Output: Standard discount: 5.0