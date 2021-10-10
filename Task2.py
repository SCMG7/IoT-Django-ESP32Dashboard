def menu():
    print("                                ************MAIN MENU************")
    print("                                 **********           ********** ")
    print("                                  ********             ******** ")
    print()
    choice = input("""
1: The identifier of the staff member who initiated the access period
2: Start date and time and end date and time of the access period
3: Approximate number of seconds the access period lasted
4: The highest temperature recorded in that access period
5: The lowest calculated dew point temperature duringthat access period
6: A list of all the recorded readings during the access period, with a calculated dew point temperature at each reading
7: Quit/Log Out

Please enter your choice: """) ## Print the Menu and asking the user for his input 1-6
    if choice == "1":
        Option1()
    elif choice == "2":
        Option2()
    elif choice == "3":
        Option3()
    elif choice == "4":        # Those are the 7 choices that the user has.
        Option4()
    elif choice == "5":
        Option5()
    elif choice == "6":
        Option6()
    elif choice == "7":
        Option7
    else:
        print("You must only select from 1-7.")
        print("Please try again")
        menu()
def Option1():                      # The identifier of the staff member who initiated the access period

    file = open('log.txt', 'r')                                # Open the log file in Read mode as 'file'
    for line in file:
        fields = line.split(",")                               # Split line where ","
        field0 = fields[0]                                     # Select only first attribute inside the file
    print(field0+"has initiated the access period ")           # Print it
    input("\nPress ENTER key to return to main menu")          # Ask the user for input in order to go back in main menu
    menu()  # Display again menu
def Option2():                      #Start date and time and end date and time of the access period

    with open('log.txt', 'r') as file:                         # Open the log file in Read mod as 'file'
        first_line = file.readline()                           # read the first line of the file
        for last_line in file:
            pass
        fields = last_line.split(",")                          # Split line where "," of the last line of the text file
        fields2 = first_line.split(",")                        # Split line where "," of the first line of the text file
        Ldate = fields[1]                                      # Get the second attribute of last line
        Ltime = fields[2]                                      # Get the third attribute of last line
        Fdate = fields2[1]                                     # Get the second attribute of first line
        Ftime = fields2[2]                                     # Get the third attribute of first line

    print("Star of session: " + Ldate + Ltime)                 # Display the Start of the session
    print("End of session: " + Fdate + Ftime)                  # Display the End of the session
    input("\nPress ENTER key to return to main menu")          # Ask user for input in order to go back in main menu
    menu()#Display again menu

def Option3():                  # Approximate number of seconds the access period lasted

    with open('log.txt', 'r') as file:                         # Open file log.txt in read mode as 'file'
        first_line = file.readline()                           # Read first line
        for last_line in file:                                 # fOR last line
            pass
        fields = last_line.split(",")                          # Split words where ","
        fields2 = first_line.split(",")                        # Split words where ","
        Ltimer = fields[5]                                     # Take timer's reading from last line
        Ftimer = fields2[5]                                    # Take timer's reading from first line
    print("Started at:"+Ftimer+"Ended at:"+Ltimer)             # Dsiplay the start and end time
    First_reading = float(input("Please insert the 'Start' seconds:"))  # ask the user to input the start seconds
    Last_reading = float(input("Please insert the 'End' seconds:"))     # ask the user to input the end seconds
    AvrgSEC = (Last_reading - First_reading)                   # Calculate an average of seconds
    print("The access period in seconds lasted an average of")
    print(AvrgSEC)                                             # Print the result
    input("\nPress ENTER key to return to main menu")          # Ask the user for input in order to go back in main menu
    menu()
def Option4():                #The highest temperature recorded in that access period

    with open('log.txt', 'r') as file:                          # Open file log.txt in read mode as 'file'
        MList = []                                              # Create List named MList
        for line in file:                                       # For every line in file (log.txt)
            fields = line.split(",")                            # Split words where ","
            field = fields[3]                                   # Take Temperature value
            fields = field.split("c")                           # Split the temperature value from the "c" on the end.
            field = fields[0]                                   # Take only temperature
            MList.append(field)                                 # Put all the values in the 'MList' list
        print("Highest temperature recorded.")                  # Display title
        print(max(MList))                                      # Display minimum temperature recorded.
    input("\nPress ENTER key to return to main menu")
    menu()                                                      # Ask user for input in order to go back in main menu

def Option5():                  #The lowest calculated dew point temperature duringthat access period

    with open('log.txt', 'r') as file:                          # Open file log.txt in read mode as 'file'
        LList = []                                              # Create List named MList
        for line in file:                                       # For every line in file (log.txt)
            fields = line.split(",")                            # Split words where ","
            field = fields[3]                                   # Take Temperature value
            fields = field.split("c")                           # Split the temperature value from the "c" on the end.
            field = fields[0]                                   # Take only temperature
            LList.append(field)                                 # Put all the values in the 'LList' list
            MinLList = (min(LList))                             # Address MinLList to the minimum value from LList
        print("Lowest calculated dew point recorded.")          # Display title
        print(MinLList)                                         # Display the minimum temperature
    input("\nPress ENTER key to return to main menu")           # Ask user for input in order to go back in main menu
    menu()

def Option6():#A list of all the recorded readings during the access period,
                # with a calculated dew point temperature at each reading.
    print("Option6 Not Completed ")
    input("\nPress ENTER key to return to main menu")
    menu()

def Option7():      #Exit
    exit

    
menu()
