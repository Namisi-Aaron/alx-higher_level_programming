#!/usr/bin/python3
import sys
import MySQLdb

"""This script lists all states from the database hbtn_0e_0_usa"""


def dbConnect(username, password, database):
    """"Connects to a database.

    Args:
        username: the database user.
        password: the users password

    Returns:
        The connection instance.
    """
    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database,
                host='localhost',
                port=3306
                )
        print("Connected to the database successfully!")
        return connection
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = dbConnect(username, password, database)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()
