#!/usr/bin/python3
"""This script lists all cities
    from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    username = argv[1]
    database_name = argv[3]
    password = argv[2]
    query = "SELECT a.name \
             FROM cities a, states b \
             WHERE a.state_id = b.id \
             AND b.name LIKE BINARY %s \
             ORDER BY a.id ASC"
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database_name,
                         port=3306)
    cur = db.cursor()
    cur.execute(query, (argv[4],))
    results = cur.fetchall()
    cities = [row[0] for row in results]
    output = ', '.join(cities)
    print(output)
    cur.close()
    db.close()
