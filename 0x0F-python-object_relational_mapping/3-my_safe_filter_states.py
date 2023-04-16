#!/usr/bin/python3
"""
This file prints all states from the database
"""

import sys
import MySQLdb


def main():
    """
    This file use a mysql search from python
    """
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_password, db=db_name)
    cursor = db.cursor()
    # Use all the SQL you like
    fl_state_name = MySQLdb.escape_string(state_name).decode()
    sqlquery = "SELECT * FROM states WHERE states.name='" + fl_state_name + "'"
    cursor.execute(sqlquery)
    data = cursor.fetchall()

    for states in data:
        print(states)
    db.close()

if __name__ == '__main__':
    main()
