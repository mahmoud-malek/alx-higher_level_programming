#!/usr/bin/python3

""" this module filters states by user input """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if (len(argv) != 4):
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    dbName = argv[3]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName, port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
