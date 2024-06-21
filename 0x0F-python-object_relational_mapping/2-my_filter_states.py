#!/usr/bin/python3
"""This script takes in an argument
    and displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    username = argv[1]
    database_name = argv[3]
    password = argv[2]
    query = "SELECT * FROM states \
             WHERE name LIKE %s \
             ORDER BY states.id ASC"
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database_name,
                         port=3306)
    cur = db.cursor()
    cur.execute(query, (argv[4],))
    results = cur.fetchall()
    for i in results:
        print(i)
    cur.close()
    db.close()
