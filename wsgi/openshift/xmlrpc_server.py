from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
from django.http import HttpResponse
from django.db import connection

class rpc_server(object):
	"""
	Instantiates an XMLRPC Server for the incoming connection.
	Provides methods for interacting with the platform.
	"""

	dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None)

	def rpc_handler(self, request):
		if len(request.POST):
			response = HttpResponse(mimetype="application/xml")
			response.write(rpc_server.dispatcher._marshaled_dispatch(request.raw_post_data))
			# DEBUG
			methods = rpc_server.dispatcher.system_listMethods()
			print "Incoming XMLRPC connection."
			print "Available methods: " + str(methods)
		else:
			response = HttpResponse()
			response.write("<b>This is an XMLRPC Service to Cockfosters.</b><br>")
			response.write("You need to invoke it using an XMLRPC client.<br>")
			response.write("The following methods are available:<ul>")
			methods = rpc_server.dispatcher.system_listMethods()

			for method in methods:
				sig = rpc_server.dispatcher.system_methodSignature(method)
				help = rpc_server.dispatcher.system_methodHelp(method)
				response.write("<li><b>%s</b>: [%s] %s" % (method, sig, help))

			response.write("</ul>")

		response['Content-length'] = str(len(response.content))
		return response

	def commit_data(id_num, id_val):
		"""
		Commits data from the client into the RHUI usage database
		"""
		sql = 'INSERT INTO test_data (id, value) VALUES (' + str(id_num) + ', ' + str(id_val) + ');'
		# DEBUG
		print "Value for id_num is: ", id_num
		print "Value for id_val is: ", id_val
		print "Value for SQL STATEMENT is: ", sql
		cursor = connection.cursor()
		cursor.execute(sql)
		return True

	def db_read():
		"""
		Pulls all of the individual records out of the database
		"""
		sql = 'SELECT * FROM test_data;'
		cursor = connection.cursor()
		cursor.execute(sql)
		db_out = cursor.fetchall()
		return db_out

	def print_this():
		"""
		Some other function
		"""
		this = "Printing THIS"
		print this
		return this

	dispatcher.register_function(commit_data, 'commit_data')
	dispatcher.register_function(print_this, 'print_this')
	dispatcher.register_function(db_read, 'db_read')

