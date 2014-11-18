#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Robin Wen
# Date: 2014-11-18
# Desc: Connect to MySQL using MySQLdb package, and insert the image to MySQL.

# Before use this scripts, login as robin into mysql, and execute:
# mysql> CREATE TABLE Images(Id INT PRIMARY KEY, Data MEDIUMBLOB);

import MySQLdb as mdb

def read_image():

    fin = open("test.png")    
    img = fin.read()

    return img

con = mdb.connect(host='10.10.3.121', user='robin', passwd='robin89@DBA', db='testdb', unix_socket='/tmp/mysql5173.sock', port=5173)


with con:
    
    cur = con.cursor()
    data = read_image()
    cur.execute("INSERT INTO Images VALUES(1, %s)", (data, ))

    print 'Number of rows inserted:', cur.rowcount

con.close()
