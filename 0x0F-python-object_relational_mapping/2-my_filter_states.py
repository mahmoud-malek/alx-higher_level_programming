#!/usr/bin/python3

""" a script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument. """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if (len(argv) != 5):
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    username = argv[1]
    password = argv[2]
    dbName = argv[3]
    value = argv[4]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbName, port=3306)
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(value))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
