#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    match = cur.fetchall()
    for name in match:
        if name[1] == sys.argv[4]:
            print(name)
    cur.close()
    db.close()
