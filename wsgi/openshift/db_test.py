# Testing whether the DB connection works. Kind of.

def db_test():
  try:
    import MySQLdb
    result = "MySQLdb imported"
  except:
    result = "MySQLdb NOT imported"

  return result

