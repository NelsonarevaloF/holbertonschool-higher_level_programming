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

    cur.execute("""SELECT cities.name FROM cities
                LEFT JOIN states ON cities.state_id=states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;""", (arg[4],))
    rows = cur.fetchall()
    aux_list = []
    for row in rows:
        aux_list.append(row[0])
    print(", ".join(aux_list))
    cur.close()
    db.close()
