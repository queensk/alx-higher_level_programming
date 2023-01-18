#!/usr/bin/python3
"""
To prevent SQL injection attacks, it is important to use parameterized,
queries when executing SQL statements. This involves using placeholders,
in the SQL query, and passing the actual values as separate parameters.
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
    query = "SELECT * FROM states \
                 WHERE name LIKE BINARY %s \
                 ORDER BY states.id ASC"
    cursor.execute(query, (argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
