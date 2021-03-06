#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Robin Wen
# Date: 2014-11-18
# Desc: Connect to MySQL using MySQLdb package, and retrieve the data of Writers table using the dictionary cursor.

import MySQLdb as mdb

con = mdb.connect(host='10.10.3.121', user='robin', passwd='robin89@DBA', db='testdb', unix_socket='/tmp/mysql5173.sock', port=5173)

with con:
    
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Writers LIMIT 4")
    
    rows = cur.fetchall()

    for row in rows:
        print row["Id"], row["Name"]

con.close()
