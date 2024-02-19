#!/usr/bin/python3

"""
This module lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    state_name = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name\
            FROM states, cities\
            WHERE states.id = cities.state_id\
            AND states.name = %s\
            ORDER BY cities.id", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
