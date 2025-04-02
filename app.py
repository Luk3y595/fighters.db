# docstring - Luke Thompson - airplane database application
# imports
import sqlite3

# constants and variables
DATABASE = "fighters.db"

# functions
def print_all_aircraft():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()    


def print_all_aircraft_by_speed():
    '''print all the aircraft sorted by the speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()


def print_all_aircraft_by_g():
    '''print all the aircraft sorted by the max g force'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY max_g DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()


def print_all_aircraft_by_climb():
    '''print all the aircraft sorted by the climbrate'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY climbrate DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()


def print_all_aircraft_by_range():
    '''print all the aircraft sorted by the range'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()


def print_all_aircraft_by_payload():
    '''print all the aircraft sorted by the payload'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter ORDER BY payload DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print("name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# main code
while True:
    user_input = input("\nWhat would you like to do. \n1. Print all aircraft \n2. Print all aircraft by speed\n3. Print all aircraft by max g force\n4. Print all aircraft by climbrate\n5. Print all aircraft by range\n6. Print all aircraft by payload\n7. Exit\n")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_g()
    elif user_input == "4":
        print_all_aircraft_by_climb()
    elif user_input == "5":
        print_all_aircraft_by_range()
    elif user_input == "6":
        print_all_aircraft_by_payload()
    elif user_input == "7":
        break 
    else:
        print("That was not an option\n")
