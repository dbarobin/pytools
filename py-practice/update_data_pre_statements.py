#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Robin Wen
# Date: 2014-11-18
# Desc: Connect to MySQL using MySQLdb package, and update the Writers table using prepared statements.

import MySQLdb as mdb

con = mdb.connect(host='10.10.3.121', user='robin', passwd='robin89@DBA', db='testdb', unix_socket='/tmp/mysql5173.sock', port=5173)

with con:
    
    cur = con.cursor()
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
        ("Guy de Maupasant", "4"))


    print 'Number of rows updated:', cur.rowcount

con.close()
