#!/usr/bin/python3
"""a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    res = cur.fetchall()
    for row in res:
        print(row)
