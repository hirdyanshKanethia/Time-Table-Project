
import os
import random
import pandas as pd
from tabulate import tabulate



def subjects():
    global subj_list
    print('''\nEnter the subjects one by one 
Enter 0 once you have entered all your subjects''')
    subj_list = []
    for i in range(1000):
        subj = input(f"Subject {i+1}: ")
        if subj == '0':
            break
        else:
            subj_list.append(subj.strip().capitalize())
    
    print("\nThis is your list of subjects ->")
    for i in range(len(subj_list)):
        print(f"Subject {i+1}: {subj_list[i]}")
    
    while True:
        choice = input('''\nDo you want to remake your subject list?
Enter y to remake the list and n to move ahead with the current subject list: ''')
        if choice.lower() == 'y':
            subjects()
        elif choice.lower().strip() == 'n':
            print("\nNow moving ahead with the current subject list")
            break
        elif ValueError:
            print("\nInvalid Input! Please enter a valid input")
        else:
            print("\nInvalid Input! Please enter a valid input")



def printtable():
    print("\nThis is your TIME TABLE")
    global data
    df = pd.DataFrame(data)
    table = tabulate(df, headers= 'keys', tablefmt='pretty', showindex=False)
    print(table)



def customize():
    global subj_list
    global choice
    try: 
        while True:
            choice = int(input('''\nDO YOU WANT TO MAKE ANY CHANGE IN THE CURRENT TIME TABLE
Enter 1 to shuffle the subjects of your TIME TABLE: 
Enter 2 to manually enter data in slots: 
Enter 3 to save your TIME TABLE:
NOTE - any manually entered data will be erased upon shuffling choice of the table i.e- option 1
Enter your choice -> '''))  # Add a choice to remove a subject from the list, add a subject to the list, show subj_list
            if choice >=1 and choice <=3:
                break
            else:
                print("\nInvalid Input! Please enter a valid choice")
    except ValueError:
        print("\nInvalid Input! Please enter a valid choice")
        customize()

    if choice == 1:
        shuffle()
        printtable()

    elif choice == 2:
        switch()
            



def switch():
    global data
    global group
    global subj_list
    try: 
        while True:
            column_choice = int(input('''\nEnter the column in which the desired slot lies that you want to enter data in: 
Enter 0 to change the time column 
Enter 1 to change the Day 1 column
Enter 2 to change the Day 2 column
Enter 3 to change the Day 3 column -> '''))
            if column_choice <= 3 and column_choice >= 0:
                break
            else:
                print("\nInvalid Input! Please enter a valid entry")
    except ValueError:
        print("\nInvalid Input! Please enter a valid entry")
    
    try:
        while True:
            row_choice = int(input("Enter the row in which the slot lies that you want to enter data in: "))
            if row_choice <= len(data["Time"]) and row_choice >= 1:
                break
            else:
                print("\nInvalid Input! Please enter a valid entry")
    except ValueError:
        print("\nInvalid Input! Please enter a valid entry")

    switch_entry = input("Enter what you want to enter in the slot described above: ")
    key = list(data.keys())
    data[key[column_choice]][row_choice - 1] = switch_entry.strip().capitalize()
    printtable()


def shuffle():
    global data
    global subj_list
    data = {
        'Time':['5:00 - 5:45', '5:45 - 6:00', '6:00 - 6:30', '6:30 - 6:45', '6:45 - 7:30'],
        'Day1':[random.choice(subj_list), 'BREAK', random.choice(subj_list), 'BREAK', random.choice(subj_list)],
        'Day2':[random.choice(subj_list), 'BREAK', random.choice(subj_list), 'BREAK', random.choice(subj_list)],
        'Day3':[random.choice(subj_list), 'BREAK', random.choice(subj_list), 'BREAK', random.choice(subj_list)]
    }











# ************************** MAIN ********************************

subjects()
shuffle()
printtable()

while True:
    customize()
    global choice 
    if choice == 3:
        break


while True:
    try:
        filename = input('''\nEnter the name of the file in which you want to save the time table:
NOTE - there should be no other file of the same name that you entered or the file may get replaced
Enter the file name here -> ''')
        if (filename == '') or (filename.isdigit() == True) or (' ' in filename.strip()) or (filename == ValueError):
            print("\nInvalid name for the file! Please enter a valid name ")
        elif filename.strip().endswith(".txt") == False:
            print("\nPlease do write '.txt' in the end of the file name ")
        elif ' ' in filename:
            print("\nSpace characters are not allowed in the name of a file")
        else:
            break
    except ValueError:
        print("\nInvalid name for the file! Please enter a valid name ")

filepath = "C:"
fullpath = os.path.join(filepath, filename.strip())

file = open(fullpath, 'w+')

global data
df = pd.DataFrame(data)
table = tabulate(df, headers= 'keys', tablefmt='pretty', showindex=False)
file.write(table)
print("File has been succesfully saved")
file.close()
print("Thank you for using the program :)")
exit()



    
