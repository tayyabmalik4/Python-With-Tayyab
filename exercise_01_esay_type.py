# **************************************************AGE Exercise****************************************************


# creating function to use again
def chkage():
    # ////creating user input
    age=int(input("Enter your age in years:   "))

    # creating condion the age is valid or not
    if age>0 and age<100:
        output=100-age
        print(f"your age 100 years after {output} years")
    # /////if age is in date of birth then calling this function
    elif age>1900 and age<2200:
        output=age+100
        print(f"The year when you are 100 years old ",output)
    # ////if value is uper or lower than we use this to make genius program and pythonic
    elif age>100 or age<1900 or age>2200:
        print("you are not born yet")
    # /////if the user input is wrong then this statement is calling
    else:
        print("Your input is wrong Please Try Again")
# /////it is optional if the user chk the age according up to own
    print("you just write a year and i will tell you : how your age in this year:")
    print("If you want to check this press key 1 other wise to press any key:")
    n=int(input())
    if n==1:
        # creating the input which you are born 
        age2=int(input("Enter the Age When You born---Age is the 1900 to 2200:   "))
        # ////creating condition and check that the user input is valid or not
        if age2>1900 and age2<2200:
            year=int(input("Enter the Year Which we want to check it:   "))
            # ////creating condition and check that the user input is valid or not
            if year>age2:
                age3=year-age2
                print(f"Your Age is {age3} in {year}")
            else:
                print("your input is wrong and your age is larger the year")
        else:
            print("You are not born Yet")
    else:
        print("Thank You to Visit My Site")
    # /////creating the input which user run again the program or not
    n1=int(input("if we want to run again the program than press key 1 otherwise press any other key:   "))
    if n1==1:
        chkage()
    else:
        print("Thanks!")
# //////calling function
chkage()
    
