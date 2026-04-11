def get_grade(score):
    """Converts a numeric score into a letter grade."""
    if score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
        return "C"
     
get_grade(85)