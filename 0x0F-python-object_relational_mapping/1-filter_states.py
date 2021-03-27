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

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                "ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
