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
	response.write("Usage Data: <br>")
	report = usage_data.objects.all()
	for line in report:
		response.write("%s, %s" % (line.uuid, line.hostname))
		response.write("<br>")
	return response
		
@csrf_exempt
def xmlrpc_handler(request):
	server = rhui_rpc_server()
	return HttpResponse(server.rpc_handler(request))
