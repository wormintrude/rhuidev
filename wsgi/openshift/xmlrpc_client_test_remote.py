import xmlrpclib

try:
	rpc_server = xmlrpclib.ServerProxy("http://rhuidev-lvecchio.rhcloud.com/rhui_xmlrpc_server/")
except:
	print "Could not contact the XMLRPC Server"

try:
	rpc_server.print_this()
	db_out = rpc_server.db_read()
	print str(db_out)
except:
	print "Some kind of error"

