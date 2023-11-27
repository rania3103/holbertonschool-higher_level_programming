#!/usr/bin/python3
""" write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name
matches the argument. But this time, write one that
is safe from MySQL injections!"""
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
    ph = "SELECT * FROM states WHERE name ="
    cur.execute(
        ph + " %(statename)s ORDER BY id;", {'statename': argv[4]})
    res = cur.fetchall()
    for row in res:
        print(row)
