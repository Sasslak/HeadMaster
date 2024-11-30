from style.color import setcolor
import datetime
from persiantools.jdatetime import JalaliDate

# Show list

def list(dB_list):
    if dB_list == None:
        print(setcolor('The list is empty!', 'red'))
    else:
        # Print header
        print(setcolor('ID     DATE         TIME       Order      Tasks ', 'cyan'))
        print(setcolor('--     ----         ----       -----      -----', 'red'))
        # Loop for print annything in database
        for tpl in dB_list:
            print(setcolor(f'{str(tpl[0]).zfill(2)}     {tpl[1]}   {tpl[2]}      {tpl[3]}          {tpl[4]}', 'yellow'))

# Add task

def add():
    # Get values of task
    task = input('Enter your task: ')
    if task != '':
        print(setcolor('1) Urgent & Important   2) Urgent & Unimportant   3) Non-Urgent & Important   4) Non-Urgent & Unimportant','cyan'))
        category = int(input('Enter your order: '))
        if 1 <= category <= 4:
            jd = str(JalaliDate.today()).replace('-','/',2)
            time = datetime.datetime.now()
            # Set dB column variable for select all column exept id column because the id is autoincrement
            dB_column = '(date, time, category, task)'
            # Change input data to a tuple for enter easier data in database
            dB_record = (jd, f'{str(time.hour).zfill(2)}:{str(time.minute).zfill(2)}', category, task)
            return dB_column, dB_record
        else:
            print(setcolor('Import valid order!','red'))
            add()
    else:
        print(setcolor('Import valid task!','red'))
        add()

# Remove task

def remove():
    return input('Enter ID or all: ').lower()

def edit():
    id = int(input('Enter ID: ').lower())
    edited_task = input('Enter new task: ').lower()
    return edited_task, id
