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
    print(f"name                          speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()    





# main code
print_all_aircraft()
