#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Robin Wen
# Date: 2014-11-18
# Desc: Connect to MySQL using MySQLdb package, and read the image to MySQL.

# Before use this scripts, login as robin into mysql, and execute:
# mysql> CREATE TABLE Images(Id INT PRIMARY KEY, Data MEDIUMBLOB);

import MySQLdb as mdb

def writeImage(data):

    fout = open('testbak.png', 'wb')    

    with fout:
        fout.write(data)

con = mdb.connect(host='10.10.3.121', user='robin', passwd='robin89@DBA', db='testdb', unix_socket='/tmp/mysql5173.sock', port=5173)


with con:
    
    cur = con.cursor()

    cur.execute("SELECT Data FROM Images WHERE Id=1")
    data = cur.fetchone()[0]
    writeImage(data)

con.close()
