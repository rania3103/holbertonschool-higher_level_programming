#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""
from MySQLdb import connect
from sys import argv


def filter_info_by_inp(username, pwd, dbname, statename):
    """conncet to db and run the query then print the result"""
    db = connect(
        host="localhost",
        user=username,
        password=pwd,
        database=dbname,
        port=3306
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id;".format(statename))
    res = cur.fetchall()
    for row in res:
        print(row)


if __name__ == "__main__":
    filter_info_by_inp(argv[1], argv[2], argv[3], argv[4])
