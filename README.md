# PyTools-By Robin Wen #

## Project Summary ##

> Tools of Python. This scripts collected via work. You may get massive useful skills throgh the script.

## Version Information ##
> Majority of scripts pass-test in Python 2.6, you'd better use Python 2.6 to run this script. I will give clear indication of this scripts in the **Scripts and Dirs Summary**.

## Change Log ##

2014-06-11
> Documentation version is **1.0**, Documentation name is **PyTools-By Robin Wen**, Comment is **Initialize the repo**, By Robin。

2014-11-17
> Documentation version is **2.0**, Documentation name is **PyTools-By Robin Wen**, Comment is **All of Scripts pass-test**, By Robin。

2014-11-18
> Documentation version is **2.1**, Documentation name is **PyTools-By Robin Wen**, Comment is **Add practice python scripts**, By Robin。

## Lists of File ##

* Squared.py [python]
* py-practice [d]
	* conn_mysql.py [python]
	* conn_mysql_new.py [python]
	* insert_data.py [python]
	* insert_images.py [python]
	* read_images.py [python]
	* retrieve_data.py [python]
	* retrieve_data_column_header.py [python]
	* retrieve_data_dict_cur.py [python]
	* retrieve_data_onebyone.py [python]
	* test_trans_support.py [python]
	* update_data_pre_statements.py [python]


## Scripts and Dirs Summary ##

### Squared.py [python] ###
> The totality of pattern lock on the phone. Use this script in Python 2.6.

### py-practice [d] ###
> Practice programming with python. Use MySQLdb plugin to connect with MySQL, and do some interaction with it, such obtain the version of database, insert data, insert image and retrieve data with multiple ways. Use this script in Python 2.7.5. This script ref: http://zetcode.com/db/mysqlpython/

#### conn_mysql.py [python] ####
> Connect to MySQL using _mysql package, and get the version of MySQL database.

#### conn_mysql_new.py [python] ####
> Connect to MySQL using MySQLdb package, and get the version of MySQL database.

#### insert_data.py [python] ####
> Connect to MySQL using MySQLdb package, and insert test data.

#### insert_images.py [python] ####
> Connect to MySQL using MySQLdb package, and insert the image to MySQL.
> Before use this scripts, login as robin into mysql, and execute:

```sql
	mysql> CREATE TABLE Images(Id INT PRIMARY KEY, Data MEDIUMBLOB);
```

#### read_images.py [python] ####
> Connect to MySQL using MySQLdb package, and read the image to MySQL.
> Before use this scripts, login as robin into mysql, and execute:

``` sql
	mysql> CREATE TABLE Images(Id INT PRIMARY KEY, Data MEDIUMBLOB);
```

#### retrieve_data.py [python] ####
>  Connect to MySQL using MySQLdb package, and retrieve the data of Writers table.

#### retrieve_data_column_header.py [python] ####
> Connect to MySQL using MySQLdb package, retrieve the data of Writers table, and make graceful display using column header.

#### retrieve_data_dict_cur.py [python] ####
> Connect to MySQL using MySQLdb package, and retrieve the data of Writers table using the dictionary cursor.

#### retrieve_data_onebyone.py [python] ####
> Connect to MySQL using MySQLdb package, and retrieve the data of Writers table using rowcount, thus display one by one.

#### test_trans_support.py [python] ####
> Connect to MySQL using MySQLdb package, and test the transaction support.

#### update_data_pre_statements.py [python] ####
> Connect to MySQL using MySQLdb package, and update the Writers table using prepared statements.

Enjoy!

## About Author ##

温国兵

* Robin Wen
* Gmail：blockxyz@gmail.com
* Blog：http://dbarobin.com
* GitHub：https://github.com/dbarobin
