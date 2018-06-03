from django.http import HttpResponse
from django.shortcuts import render
from .models import Codigoestadohistorico, SitiosPhishing, Ipwhois, Email

def home(request):
	return render(request,"index.html")

def monito(request):
	sph = SitiosPhishing.objects.all.filter(estatus='no reportado').order_by('id_sitio').first()
	print sph
	# ceh = Codigoestadohistorico.objects.order_by('')
	# return render(request,"monitor.html",{'Codigoestadohistorico':ceh, 'SitiosPhishing': sph, 'Ipwhois': ipwho, 'Email':email})
	return render(request, "monitor.html".{'SitiosPhishing':sph})
def historico(request):
	return render(request,"historico.html")

def reportes(request):
	return render(request,"reportes.html")

def verifica(request):
	return render(request,"verifica.html")

def monito_list(request):
	return render(request, )