#!/usr/bin/python3
"""
This module filter states table and select some content
"""

import sys
import MySQLdb as sql


def select_states():
    """
    This method Uses mySQL queries to select states
    """
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    connection = sql.connect(host=host, user=user,
                             passwd=passwd, db=sys.argv[3], port=port)
    cur = connection.cursur()
    sql_command = 'SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;'
    cur.execute(sql_command)
    result = cur.fetchall()
    cur.close()
    connection.close()

    if result:
        for states in result:
            print(states)


if __name__ == '__main__':
    select_states()