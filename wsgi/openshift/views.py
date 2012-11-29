import os
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def report(request):
    html_response = "Reporte de consumo de horas RHUI"
    return HttpResponse(html_response)

def rhui_xmlrpc_handler(request):
    html_response = "Interfaz de comunicacion con clientes RHUI"
    return HttpResponse(html_response)

