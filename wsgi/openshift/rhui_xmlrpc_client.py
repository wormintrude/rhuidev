import xmlrpclib

conn = xmlrpclib.ServerProxy("http://localhost:8000/rhui_xmlrpc_server/")
conn.db_read()
