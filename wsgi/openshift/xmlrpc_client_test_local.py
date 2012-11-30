import xmlrpclib

class rpc_connect(object):
	def rpc_server():
		try:
			rpc_server = xmlrpclib.ServerProxy("http://localhost:8000/rhui_xmlrpc_server/")
		except:
			print "Could not connect to XMLRPC Server"

	def commit_to_db(id_num, id_val):
		try:
			rpc_connect.rpc_server.commit_data(id_num, id_val)
			result = "Data commited"
		except:
			result = "Failed to commit data"
		
		return result

