#Convert month name to days - Andy Ha 20220606

def main():
    in1 = str(input("Input the name of Month:"))

    x = in1.upper()

    print (in1.capitalize())

    if x in ("JANUARY", "MARCH", "MAY", "JUNE" , "AUGUST", "OCTOBER", "DECEMBER"):
        print ("No. of days: 31 days")
    
    elif x == "FEBRUARY":
        print (" No. of days: 29 days")
    else:
        print("No. of days: 30 days")

    
    in2= str(input("Would you like to know the amount of days for another month? (Yes/No)"))
    y = in2.upper()
    if y == ("YES"):
        main()
    elif y == ("NO"):
        return()
    else: 
        in3=str(input("Invalid Answer. Try again? Yes/No"))

    z = in3.upper()
    if z == "YES":
        main() 
    else: 
        return()
        
    
main()

#If you want to repeat a loop you have to define it. This is the furthest I can make my loop at this point without confusing myself. I wanted there to be multiple options available incase you wanted to ask the question again.
