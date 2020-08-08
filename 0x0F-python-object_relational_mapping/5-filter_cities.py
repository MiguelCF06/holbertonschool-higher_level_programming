#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
    cities.state_id = states.id WHERE states.name LIKE %s ORDER BY \
    cities.id ASC", (sys.argv[4],))
    values = cur.fetchall()
    length = len(values)
    print(", ".join(value[0] for value in values))
    cur.close()
    db.close()
