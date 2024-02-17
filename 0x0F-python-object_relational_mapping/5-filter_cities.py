#!/usr/bin/python3

"""script that takes in the name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa"""

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
    query = ("SELECT cities.name FROM cities JOIN states ON "
             "cities.state_id = states.id WHERE states.name = %s ORDER BY "
             "cities.id ASC")
    cur.execute(query, (value,))

    rows = cur.fetchall()

    for row in rows:
        for col in row:
            print(col, end="")
        print(", " if row != rows[-1] else "\n", end="")

    cur.close()
    db.close()
