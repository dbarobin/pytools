#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Robin Wen
# Date: 2014-11-18
# Desc: Connect to MySQL using MySQLdb package, and test the transaction support.

import MySQLdb as mdb
import sys


try:
    con = mdb.connect(host='10.10.3.121', user='robin', passwd='robin89@DBA', db='testdb', unix_socket='/tmp/mysql5173.sock', port=5173)

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25)) ENGINE=INNODB")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Terry Pratchett')")
    
    con.commit()
    
except mdb.Error, e:
  
    if con:
        con.rollback()
        
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()
