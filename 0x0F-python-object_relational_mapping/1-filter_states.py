#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
"""

import sys
import MySQLdb

if __name__ == '__main__':
    """
    access the database and update state.
    """
    mySql_username = sys.argv[1]
    mySql_password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mySql_username,
        password=mySql_password,
        db=database_name,
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
