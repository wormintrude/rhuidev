import os
from django.http import HttpResponse
from django.shortcuts import render_to_response
from db_test import db_test

def home(request):
    return render_to_response('home/home.html')

def report(request):
    html_response = "Reporte de consumo de horas RHUI"
    return HttpResponse(html_response)

def rhui_xmlrpc_handler(request):
    html_response = "Interfaz de comunicacion con clientes RHUI"
    return HttpResponse(html_response)

def rhui_db_test(request):
    test = db_test()
    return HttpResponse(test.db_connection_test())

def rhui_db_read_test(request):
    test = db_test()
    return HttpResponse(test.db_read_test())

def rhui_db_write_test(request):
    test = db_test()
    return HttpResponse(test.db_write_test())

