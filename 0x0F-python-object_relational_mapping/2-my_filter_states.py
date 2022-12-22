#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    access the database and update state
    """
    mySql_username = argv[1]
    mySql_password = argv[2]
    database_name = argv[3]
    search_state = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mySql_username,
        passwd=mySql_password,
        db=database_name
    )

    cursor = db.cursor()
    query = 'SELECT * FROM states \
            WHERE name = "{}" \
            ORDER BY id ASC'.format(search_state)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
