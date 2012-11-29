# Testing whether the DB connection works. Kind of.

import MySQLdb as mysqldb
import os

class db_test(object):
  def db_connection_test(self):
    try:
      import MySQLdb
      result = "MySQLdb imported succesfully"
    except:
      result = "MySQLdb NOT imported"

    return result

  def db_read_test(self):
    try:
      database = mysqldb.connect(host=os.environ['OPENSHIFT_MYSQL_DB_HOST'], user=os.environ['OPENSHIFT_MYSQL_DB_USERNAME'], passwd=os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'], db=os.environ['OPENSHIFT_APP_NAME'])
      # database = mysqldb.connect(host='localhost', user='admin', passwd='iJlhrsX4pAYp', db='rhuidev')
      cursor = database.cursor()
      sql = 'SELECT * FROM rhuidev.usage_data;'
      cursor.execute(sql)
      result = cursor.fetchall()
      ## DEBUG
      # print sql
      # print result
      # print type(result)
    except:
      result = "Error reading database"

    return result

  def db_write_test(self):
    try:
      database = mysqldb.connect(host='localhost', user='admin', passwd='iJlhrsX4pAYp', db='rhuidev')
      sql = 'CREATE TABLE db_write_test (some_field VARCHAR(4));'
      result = database.query(sql)
    except:
      result = "Error writing to database"
   
    return result

