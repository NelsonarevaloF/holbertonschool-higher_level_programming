#!/usr/bin/python3


'''this module sets connection with the BD and shows the date
that start witn N'''


import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(host="localhost", user=arg[1],
                         passwd=arg[2], db=arg[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                LEFT JOIN states ON cities.state_id=states.id
                ORDER BY cities.id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
