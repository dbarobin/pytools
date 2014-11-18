#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Robin Wen
# Date: 2014-11-18
# Desc: Connect to MySQL using _mysql package, and get the version of MySQL database.

import _mysql
import sys

try:
    con = _mysql.connect(host='10.10.3.121', user='robin', passwd='robin89@DBA', db='testdb', unix_socket='/tmp/mysql5173.sock', port=5173)
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print "MySQL version: %s" % \
        result.fetch_row()[0]
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

con.close()
