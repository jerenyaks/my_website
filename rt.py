def get_grade(score):    
if score >= 90:         
 print("A")    
elif score >= 75:        
 print("B")    
elif score >= 60:       
 print("C")   
 # print won't execute if the function returns before it reaches this line therefore it is impure and wont display the grade if the score is above 60   
#by putting the return statement before the print statement we have made the function impure because it will not execute the print statement if the score is above 60 and it will not display the grade for scores above 60.



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