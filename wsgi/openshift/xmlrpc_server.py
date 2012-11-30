from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
from django.http import HttpResponse

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

	def commit_data(self, data):
		"""
		Commits data from the client into the RHUI usage database
		"""
		print data
		return 0

	def print_this(self, data):
		"""
		Some other function
		"""
		print data

	dispatcher.register_function(commit_data, 'commit_data')
	dispatcher.register_function(print_this, 'print_this')

