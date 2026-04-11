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
describe_temp(30)