# Testing whether the DB connection works. Kind of.

import MySQLdb as mysqldb

class db_test(object):
  def db_test(self):
    try:
      import MySQLdb
      result = "MySQLdb imported succesfully"
    except:
      result = "MySQLdb NOT imported"

    return result

  def db_read_test(self):
    try:
      database = mysqldb.connect(host='localhost', user='admin', passwd='', db='rhuidev')
    except:

    return result

  def db_write_test(self):
    try:
    except:
   
    return result

