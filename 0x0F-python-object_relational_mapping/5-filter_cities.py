#!/usr/bin/python3
"""
This module uses the MySQLdb module to execute SQL commands.
(Best way to access database in python)
It does operations on @cities and @states Table
"""
import sys
import MySQLdb as sql


def filter_cities():
    """This method Uses mySQL queries to filter cities"""
    host = "localhost"
    port = 3306
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state1 = sys.argv[4]
    connection = sql.connect(host=host, user=username,
                             passwd=passwd, db=database, port=port)
    cur = connection.cursor()
    cur.execute('SELECT c.name FROM cities c INNER JOIN states s ' +
                'ON s.id = c.state_id WHERE ' +
                'BINARY s.name = %s ' +
                'ORDER BY c.id ASC;', [state1])
    result = cur.fetchall()

    if result:
        for states in result:
            print(states, end="")
        print()
    cur.close()
    connection.close()


if __name__ == '__main__':
    filter_cities()
