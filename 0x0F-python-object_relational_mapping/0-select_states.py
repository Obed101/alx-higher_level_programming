#!/usr/bin/python3
"""
This module uses the MySQLdb module to execute SQL commands.
(Best way to access database in python)
"""
import sys
import MySQLdb as sql


def select_states():
    """This method Uses mySQL queries to select states"""
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    connection = sql.connect(host=host, user=user,
                             passwd=passwd, db=sys.argv[3], port=port)
    cur = connection.cursur()
    sql_command = 'SELECT * FROM states ORDER BY id ASC;'
    cur.execute(sql_command)
    result = cur.fetchall()

    if result:
        for states in result:
            print(states)
    cur.close()
    connection.close()


if __name__ == '__main__':
    select_states()
