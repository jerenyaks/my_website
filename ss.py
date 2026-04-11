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