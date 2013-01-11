from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
from django.http import HttpResponse
from rhui_db.models import usage_data

class rhui_rpc_server(object):
	"""
	Instantiates an XMLRPC Server for the incoming connection.
	Provides methods for interacting with the platform.
	"""

	dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None)

	def rpc_handler(self, request):
		if len(request.POST):
			response = HttpResponse(mimetype="application/xml")
			response.write(rhui_rpc_server.dispatcher._marshaled_dispatch(request.raw_post_data))
			## DEBUG
			#methods = rhui_rpc_server.dispatcher.system_listMethods()
			#print "Incoming XMLRPC connection."
			#print "Available methods: " + str(methods)
		else:
			response = HttpResponse()
			response.write("<b>This is an XMLRPC Service to Cockfosters.</b><br>")
			response.write("You need to invoke it using an XMLRPC client.<br>")
			response.write("The following methods are available:<ul>")
			methods = rhui_rpc_server.dispatcher.system_listMethods()

			for method in methods:
				sig = rhui_rpc_server.dispatcher.system_methodSignature(method)
				help = rhui_rpc_server.dispatcher.system_methodHelp(method)
				response.write("<li><b>%s</b>: [%s] %s" % (method, sig, help))

			response.write("</ul>")

		response['Content-length'] = str(len(response.content))
		return response

	def commit_data(partner_name_val, partner_contact_val, end_user_name_val, end_user_country_val, end_user_postal_code_val, end_user_contact_val, uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, virtual_guests_val):
		"""
		Commits data from the client into the RHUI usage database
		"""
		entry = usage_data(partner_name = str(partner_name_val), partner_contact = str(partner_contact_val), end_user_name = str(end_user_name_val), end_user_country = str(end_user_country_val), end_user_postal_code = str(end_user_postal_code_val), end_user_contract = str(end_user_contact_val), uuid = str(uuid_val), hostname = str(hostname_val), cpus = int(cpus_val), is_virtual = is_virtual_val, ent_virtual = ent_virtual_val, ent_cluster = ent_cluster_val, ent_lvs = ent_lvs_val, ent_resilient = ent_resilient_val, ent_scalable = ent_scalable_val, ent_hpn = ent_hpn_val, virtual_guests = virtual_guests_val)
		try:
			entry.save()
			return True
		except:
			return False

	def db_read():
		"""
		Pulls all of the individual records out of the database
		"""
		db_out = usage_data.objects.all()
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

