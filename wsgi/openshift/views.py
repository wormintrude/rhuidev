import os
from django.http import HttpResponse
from django.shortcuts import render_to_response
from rhui_xmlrpc_server import rhui_rpc_server
from rhui_db.models import usage_data

# Resolution to XMLRPC 403 issue
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render_to_response('home/home.html')

def report(request):
	html_response = "Reporte de consumo de horas RHUI"
	return HttpResponse(html_response)

def rhui_db_read_test(request):
	response = HttpResponse()
	response.write("<b>RHUI Usage Data</b><br>")
	report = usage_data.objects.all()
	response.write("<b>Total number of entries in rhuidev.rhui_db_usage_data: %s</b><br>" % (len(report)))
	response.write("Usage Data: <br>")
	for line in report:
		response.write("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (line.partner_name, line.partner_contact, line.end_user_name, line.end_user_country, line.end_user_postal_code, line.end_user_contact, line.uuid, line.hostname, line.time_stamp, line.cpus, line.is_virtual, line.ent_virtual, line.ent_cluster, line.ent_lvs, line.ent_resilient, line.ent_scalable, line.ent_hpn, line.virtual_guests))
		response.write("<br>")
	return response
		
@csrf_exempt
def xmlrpc_handler(request):
	server = rhui_rpc_server()
	return HttpResponse(server.rpc_handler(request))
