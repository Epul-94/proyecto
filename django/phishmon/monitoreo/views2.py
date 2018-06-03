# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def monito(request):
	return render(request,"monitoreo/monitor.html")

def historico(request):
	return render(request,"monitoreo/historico.html")

def reportes(request):
	return render(request,"monitoreo/reportes.html")

def verifica(request):
	return render(request,"monitoreo/verifica.html")

def home(request):
	return render(request,"monitoreo/index.html")