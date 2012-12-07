# Testing whether the DB connection works. Kind of.

import MySQLdb as mysqldb
from django.db import connection
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
			cursor = connection.cursor()
			sql = 'SELECT * FROM rhuidev.rhui_db_usage_data;'
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
			cursor = connection.cursor()
			sql = 'CREATE TABLE db_write_test (some_field VARCHAR(4));'
			result = cursor.execute(sql)
		except:
			result = "Error writing to database"
   
		return result

