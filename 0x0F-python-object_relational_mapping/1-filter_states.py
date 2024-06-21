#!/usr/bin/python3
"""This script lists all states with a name
    starting with 'N'"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    username = argv[1]
    database_name = argv[3]
    password = argv[2]
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database_name,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' \
                ORDER BY states.id ASC")
    results = cur.fetchall()
    for i in results:
        print(i)
    cur.close()
    db.close()
