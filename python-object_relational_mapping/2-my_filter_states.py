#!/usr/bin/python3
""" a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""
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
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id;".format(argv[4]))
    res = cur.fetchall()
    for row in res:
        print(row)
