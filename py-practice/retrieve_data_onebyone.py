#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Robin Wen
# Date: 2014-11-18
# Desc: Connect to MySQL using MySQLdb package, and retrieve the data of Writers table using rowcount, thus display one by one.

import MySQLdb as mdb

con = mdb.connect(host='10.10.3.121', user='robin', passwd='robin89@DBA', db='testdb', unix_socket='/tmp/mysql5173.sock', port=5173)

with con:
    
    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")
    
    for i in range(cur.rowcount):

        row = cur.fetchone()
        print row[0],row[1]

con.close()
