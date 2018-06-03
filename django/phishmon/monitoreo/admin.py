# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Codigoestadohistorico,Network,Sector,Comentarios,Entidades,Contacto,Direccion,Email,Dominiowhois,Ipwhois,Lineas,Telefono,SitiosPhishing

admin.site.register(Codigoestadohistorico)
admin.site.register(Comentarios)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Dominiowhois)
admin.site.register(Email)
admin.site.register(Entidades)
admin.site.register(Ipwhois)
admin.site.register(Lineas)
admin.site.register(Network)
admin.site.register(Sector)
admin.site.register(Telefono)
admin.site.register(SitiosPhishing)



