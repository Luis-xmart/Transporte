from django.contrib import admin
from .models import TipoVehiculo
# Register your models here.

class TipoVehiculoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    list_filter = ('nombre', 'created', 'updated')
    search_fields = ('nombre', 'created', 'updated')

admin.site.register(TipoVehiculo, TipoVehiculoAdmin)
