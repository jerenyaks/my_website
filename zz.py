
def is_even(n):
    if n % 2 == 0:
        return True
        print("It is even!")
    else:
        return False
        print("It is odd!")
        #The print statements will never be executed because they come after return statements therefore they are impure
        #the prints are basically dead code because they will never be executed and they will not display whether the number is even or odd.
        #if/else statements are not impure but the print statements after the return statements are impure because they will never be executed and they will not display whether the number is even or odd.






def is_even(n):
    """Return True if n is even, False otherwise."""
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False
        