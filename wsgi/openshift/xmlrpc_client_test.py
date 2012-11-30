import sys
import xmlrpclib

try:
	rpc_server = xmlrpclib.ServerProxy("http://localhost:8000/rhui_xmlrpc_server/")
except:
	print "Could not contact the XMLRPC Server"

try:
	data = str("some_data")
	rpc_server.print_this(data)
except:
	print "Some kind of error"

