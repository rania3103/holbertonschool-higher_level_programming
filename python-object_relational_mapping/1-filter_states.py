#!/usr/bin/python3
"""a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def filter_info(username, pwd, dbname):
    """conncet to db and run the query then print the result"""
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=pwd,
        database=dbname,
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    res = cur.fetchall()
    for row in res:
        print(row)


if __name__ == "__main__":
    filter_info(argv[1], argv[2], argv[3])
