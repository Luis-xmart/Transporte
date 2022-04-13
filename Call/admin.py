from django.contrib import admin
from .models import TipoServicio, TipoIdentificacion, FormaPago, Municipio, Departamento

# Register your models here.
class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')
    
class TipoIdentificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

admin.site.register(TipoServicio, TipoServicioAdmin)
admin.site.register(TipoIdentificacion, TipoIdentificacionAdmin)
admin.site.register(FormaPago, FormaPagoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)