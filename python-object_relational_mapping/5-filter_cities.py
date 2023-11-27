#!/usr/bin/python3
""" a script that takes in the name of a state
as an argument and lists all cities of that state"""
from MySQLdb import connect
from sys import argv


if __name__ == "__main__":
    """conncet to db and run the query then print the result"""
    db = connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )
    cur = db.cursor()
    ph1 = "SELECT DISTINCT name FROM cities WHERE state_id IN"
    ph2 = "(SELECT id FROM states WHERE name = %(statename)s)"
    cur.execute(ph1 + " " + ph2, {'statename': argv[4]})
    res = cur.fetchall()
    ch = ""
    if len(res) > 0:
        for row in res:
            ch += str(row[0]) + ", "
        print(ch[:len(ch) - 2])
    else:
        print()
