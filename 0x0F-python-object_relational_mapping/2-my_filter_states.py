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

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mySql_username,
        passwd=mySql_password,
        db=database_name,
    )

    cursor = conn.cursor()
    query = f'SELECT * FROM states \
            WHERE name = "{search_state}" \
            ORDER BY id ASC'
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
