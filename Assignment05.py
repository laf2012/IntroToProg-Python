# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <LFerrier>,<11.15.2022>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# File to List
objF = open(objFile, "r")
for row in objF:
    if len(row.strip()) == 0:
        continue
    lstRow = row.split(",") # Establish comma to separate elements per row in lstTable
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]} # Establish 2 dictionary keys w/ index values from lstRow
    lstTable.append(dicRow) # Permit additional dictionary rows to lstTable
objF.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # Add a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("All Data Stored in Temporary Memory")
        print("="*40)
        for row in lstTable:
            print(row["Task"], row["Priority"], sep=', ') # Present all rows in listTable w/ keys of Task & Priority
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Create new dicRow based off user inputs that serve as values to established keys (ref. line 31)
        dicRow = {'Task': input('\nWhat task do you want to complete? '), 'Priority': input('\nWhat is the priority of this task from 1 to 10? ')}
        lstTable.append(dicRow) # Add new dicRow to lstTable
        print() # Print lines for looks
        print("="*40)
        print(dicRow)
        print("=" * 40)
        print("Saved to temporary memory!")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input('\nEnter task you want removed ') # Define strRemove as task user wants removed
        for row in lstTable:
            if row['Task'] == strRemove:
                lstTable.remove(row) # If strRemove is a value for Task key in lstTable, remove
        print() # Print lines for looks
        print("=" * 40)
        print(dicRow)
        print("=" * 40)
        print("Task deleted!")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(objFile, 'w')
        for row in lstTable:
            objFile.write(row['Task'] + ',' + row['Priority'] + '\n')
        objFile.close()
        print('Data Saved!\n')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program