#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    username = argv[1]
    database_name = argv[3]
    password = argv[2]
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cur.fetchall()
    for i in results:
        print(i)
    cur.close()
    db.close()
