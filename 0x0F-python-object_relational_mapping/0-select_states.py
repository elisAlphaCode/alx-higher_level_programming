#!/usr/bin/python3
"""
Script that listd all `states` from the database `hbtn_0e_usa`
Aruguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
 
    db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2], db=sys.argv[3], host="localhost", port=3306)
    cur= db.cursor()

    cur.execute("SELECT * FROM states ORDER By id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
