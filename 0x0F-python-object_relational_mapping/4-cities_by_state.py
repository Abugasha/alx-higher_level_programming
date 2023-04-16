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

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_password, db=db_name)
    cursor = db.cursor()
    # Use all the SQL you like
    sqlquery = ("""SELECT cities.id, cities.name, states.name FROM states JOIN
                cities ON states.id=cities.state_id ORDER BY cities.id ASC""")
    cursor.execute(sqlquery)
    data = cursor.fetchall()

    for states in data:
        print(states)
    db.close()

if __name__ == '__main__':
    main()
