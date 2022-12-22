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

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states \
            WHERE name = "{}" \
            ORDER BY id ASC'.format(argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
