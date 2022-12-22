#!/usr/bin/python3
"""
script that takes in an argument and,
displays all values in the states table,
of hbtn_0e_0_usa where name matches the argument.
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    access the database and update state
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
