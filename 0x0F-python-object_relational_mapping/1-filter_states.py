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
    cursor.execute("""SELECT * FROM states WHERE states.name
                   LIKE BINARY 'N%' ORDER BY states.id ASC""")
    data = cursor.fetchall()

    for states in data:
        print(states)
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
