#!/usr/bin/python3

""" This module lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database_name, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
