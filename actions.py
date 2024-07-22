from style.color import setcolor
import datetime

# Show list

def list(dB_list):
    if dB_list == None:
        print(setcolor('The list is empty!', 'red'))
    else:
        # Print header
        print(setcolor('ID    DATETIME\t\t   Tasks', 'cyan'))
        print(setcolor('--    --------------\t   -----', 'red'))
        # Loop for print annything in database
        for tpl in dB_list:
            print(setcolor(f'{str(tpl[0]).zfill(2)}    {tpl[2]}\t   {tpl[1]}', 'yellow'))

# Add task

def add():
    # Get values of task
    task = input('Enter your task: ').capitalize()
    time = datetime.datetime.now()
    # Set dB column variable for select all column exept id column because the id is autoincrement
    dB_column = '(task, datetime)'
    # Change input data to a tuple for enter easier data in database
    dB_record = (
        task, f'{time.day}/{time.month}/{time.year}-{time.hour}:{time.minute}')
    return dB_column, dB_record

# Remove task

def remove():
    return input('Enter ID or all: ').lower()

def edit():
    id = int(input('Enter ID: ').lower())
    edited_task = input('Enter new task: ').lower()
    return edited_task, id