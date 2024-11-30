# Import libraries

import datetime
import database.dB as dB
import os
import sys
from style.color import setcolor
import style.loading as loading
import actions

# Clear whole console first

os.system('cls')

# Connect database / database name = task_database.db

dB_connect, dB_cursor = dB.connect_dB('database/database.db')

# Create table / table name = task_tbl

dB_tblname = 'task_tbl'
dB_feilds = '(id integer PRIMARY KEY autoincrement, date TEXT, time TEXT, category TEXT, task TEXT)'
dB.create_table(dB_connect, dB_cursor, dB_tblname, dB_feilds)

# Loading start program

print('Starting HeadMaster')
loading.start()

# Starting program

while True:
    print()
    choice = input('>>> ').lower()
    print()
    match choice:

        # Show everything in database

        case 'list' | 'show' | 'tasks' | 'ls':
            # Select all data in database
            dB_list = dB.select_data(dB_cursor, dB_tblname)
            # Print list
            actions.list(dB_list)

        # Add task to database

        case 'add' | 'insert':
            dB_column, dB_record = actions.add()
            dB.insert_data(dB_connect, dB_cursor,
                           dB_tblname, dB_column,dB_record)

        # Remove a row in database with ID or all

        case 'remove' | 'rm' | 'del' | 'delete':
            dB.remove_data(dB_connect, dB_cursor, dB_tblname, actions.remove())

        # Edit a data with ID

        case 'edit' | 'update':
            edited_task, id = actions.edit()
            dB.update_data(dB_connect, dB_cursor, dB_tblname,
                           'task', edited_task, id)

        case 'help':
            print('''Headmaster is an easy way to manage your tasks

These are Headmaster commands:
    list           Show a list of tasks
    add            Add a task to the list
    remove         Remove a task from the list
    edit           Edit a task from the list
    cls            Clear the screen
    restart        Restart the program
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
        
        case _:
            print(setcolor('Ooops! Your word is wrong','red'))

