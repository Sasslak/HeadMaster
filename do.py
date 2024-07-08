# Import libraries

import datetime
import dB
import os
import sys
import time
from colorama import Fore

# Clear whole console first

os.system('cls')

# Connect database / database name = task_database.db

dB_connect, dB_cursor = dB.connect_dB('task_database.db')

# Create table / table name = task_tbl

dB_tblname = 'task_tbl'
dB_feilds = '(id integer PRIMARY KEY autoincrement, task TEXT, datetime TEXT)'
dB.create_table(dB_connect, dB_cursor, dB_tblname, dB_feilds)

print('Starting HeadMaster')
animation = "|/-\\"
start_time = time.time()
while True:
    for i in range(4):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 0.8:
        break
sys.stdout.write("\rDone!")


# Starting program

while True:
    print()
    choice = input('>>> ').lower()
    print()
    match choice:

        # Show everything in database

        case 'list' | 'show' | 'tasks':
            # Select all data in database
            dB_list = dB.select_data(dB_cursor, dB_tblname)
            if dB_list == []:
                print(Fore.RED+'The list is empty!'+Fore.RESET)
            else:
                # Print header
                print(Fore.CYAN+'ID    DATETIME\t\t   Tasks'+Fore.RESET)
                print(Fore.RED+'--    --------------\t   -----'+Fore.RESET)
                # Loop for print annything in database
                for tpl in dB_list:
                    # 01 - 09
                    if tpl[0] < 10:
                        print(Fore.YELLOW +
                              f'0{tpl[0]}    {tpl[2]}\t   {tpl[1]}'+Fore.RESET)
                    # 10 - 99
                    elif tpl[0] < 100:
                        print(Fore.YELLOW +
                              f'{tpl[0]}    {tpl[2]}\t   {tpl[1]}'+Fore.RESET)
                    # 100 - inf
                    else:
                        print(Fore.YELLOW +
                              f'{tpl[0]}  {tpl[2]}\t   {tpl[1]}'+Fore.RESET)

        # Add task to database

        case 'add' | 'insert':
            task = input('Enter your task: ').lower()
            time = datetime.datetime.now()
            # Set dB column variable for select all column exept id column because the id is autoincrement
            dB_column = '(task, datetime)'
            # Change input data to a tuple for enter easier data in database
            dB_record = (
                task, f'{time.day}/{time.month}/{time.year}-{time.hour}:{time.minute}')
            dB.insert_data(dB_connect, dB_cursor,
                           dB_tblname, dB_column, dB_record)

        # Remove a row in database with ID or all

        case 'remove' | 'rm' | 'del' | 'delete':
            rm = input('Enter ID or all: ').lower()
            dB.remove_data(dB_connect, dB_cursor, dB_tblname, rm)

        # Edit a data with ID

        case 'edit' | 'update':
            id = input('Enter ID: ').lower()
            edited_task = input('Enter new task: ').lower()
            dB.update_data(dB_connect, dB_cursor, dB_tblname,
                           'task', edited_task, id)

        case 'help':
            print('''Headmaster is an easy way to manage your tasks

These are Headmaster commands:
    list           Show a list of tasks
    add            Add a task to the list
    remove <ID>    Remove a task from the list
    edit <ID>      Edit a task from the list
    cls            Clear the screen
    exit           Exit the program'''
            )



        # Clear screen with command

        case 'cls' | 'clear' | 'clean':
            os.system('cls')

        # Restart program

        case 'restart':
            os.execl(sys.executable, sys.executable, *sys.argv)

        # Exit from program

        case 'exit' | 'close' | 'quit':
            break