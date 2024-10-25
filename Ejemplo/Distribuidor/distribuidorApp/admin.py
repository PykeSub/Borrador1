from django.contrib import admin
from distribuidorApp.models import Distribuidores

class distribuidorAdmin(admin.ModelAdmin):
    list_display = ['telefono', 'email', 'fechaDespacho', 'fechaRecepcion', 'ciudad']
    
# Register your models here.
admin.site.register(Distribuidores, distribuidorAdmin)