#!/usr/bin/python3
"""This scriptlists all cities
    from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    username = argv[1]
    database_name = argv[3]
    password = argv[2]
    query = "SELECT a.id, a.name, b.name \
             FROM cities a, states b \
             WHERE a.state_id = b.id \
             ORDER BY a.id ASC"
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database_name,
                         port=3306)
    cur = db.cursor()
    cur.execute(query)
    results = cur.fetchall()
    for i in results:
        print(i)
    cur.close()
    db.close()
