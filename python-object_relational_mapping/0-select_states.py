#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
from MySQLdb import connect
from sys import argv


def list_info(username , pwd, dbname):
    """conncet to db and run the query then print the result"""
    db = connect(
        host="localhost",
        user=username,
        password=pwd,
        database=dbname,
        port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    res = cur.fetchall()
    for row in res:
        print(row)

if __name__ == "__main__":
    list_info(argv[1], argv[2], argv[3])
