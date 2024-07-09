import sqlite3
from sqlite3 import Error
from colorama import Fore

# Connect database

def connect_dB(path):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    return connect,cursor

# Create table

def create_table(connect,cursor,name_tbl,fields_tbl):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {name_tbl}{fields_tbl}')
    connect.commit()

# Insert data

def insert_data(connect,cursor,name_tbl,column,record,selector='*'):
    try:
        if record[0] != '':
            cursor.execute(f"INSERT INTO {name_tbl} {column} VALUES(?,?)",record)
            print(Fore.GREEN+'Successfuly added!'+Fore.RESET)
        else:
            print(Fore.RED+'Error! Add failed!(empty input)'+Fore.RESET)
    except Error:
        print(Fore.RED+'Error! Add failed! '+Fore.RESET)
    finally:
        connect.commit()

# Select data

def select_data(cursor,name_tbl,selector='*'):
    try:
        cursor.execute(f'SELECT {selector} FROM {name_tbl}')
        return cursor.fetchall()
    except Error:
        return (Fore.RED+'Error to select data!'+Fore.RESET)

# Remove data

def remove_data(connect,cursor,name_tbl,rm):
    try:
        data = select_data(cursor,name_tbl)
        if rm.isdigit():
            if int(rm) > data[-1][0] or int(rm) < data[0][0]:
                print(Fore.RED+'Error! Remove failed! (out of range)'+Fore.RESET)
            else:
                cursor.execute(f'DELETE FROM {name_tbl} WHERE id={rm}')
                print(Fore.GREEN+'Successfuly removed!'+Fore.RESET)
        elif rm == 'all':
            cursor.execute(f'DELETE FROM {name_tbl}')
            print(Fore.GREEN+'Successfuly removed!'+Fore.RESET)
    except Error:
        print(Fore.RED+'Error! Remove failed!'+Fore.RESET)
    finally:
        connect.commit()

# Update data

def update_data(connect,cursor,name_tbl,field,description,id):
    try:
        cursor.execute(f"UPDATE {name_tbl} SET {field} = '{description}' WHERE id = {id}")
        test_select = select_data(cursor,name_tbl)
        if test_select[id-1][1] == description:
            print(Fore.GREEN+'Successfuly edited!'+Fore.RESET)
        else:
            print(Fore.RED+'Error! Edit failed!'+Fore.RESET)
    except Error:
        print(Fore.RED+'Error! Edit failed!'+Fore.RESET)
    finally:
        connect.commit()