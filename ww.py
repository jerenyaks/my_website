def describe_temp(temp):
    if temp > 35:
        print("Hot")
        return "Hot"
    elif temp > 20:
        return "Warm"
    elif temp > 10:
        print("Cool")
        return "Cool"
    #print and return bring inconsistency to the function and make it pure by ensuring that it always returns a value and does not have side effects such as printing to the console.
    #by removing return statements we ensure that the function does not return any value and only has side effects such as printing to the console, making it an impure function.




def describe_temp(temp):
    """Convert a temperature value into a label of Hot, Warm, Cool, or Cold."""
    if temp > 35:
        print("Hot")
    elif temp > 20:
        print("Warm")
    elif temp > 10:
        print("Cool")
    else:
        print("Cold")
describe_temp(23)