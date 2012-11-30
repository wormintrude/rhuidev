import sys
import xmlrpclib

rpc_server = xmlrpclib.ServerProxy("http://localhost:8000/rhui_xmlrpc_server/")
try:
	result = rpc_server.commit_data()
except:
	print "Some kind of error"

