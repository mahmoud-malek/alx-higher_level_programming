#!/usr/bin/python3

""" a script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument. """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    dbName = argv[3]
    value = argv[4]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
    cur.execute(query.format(value))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
