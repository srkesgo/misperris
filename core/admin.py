from django.contrib import admin
from .models import Raza,Estado,Mascotas
# Register your models here.

#configuraremos la entidad automovil
#en el admin de django
class MascotaAdmin(admin.ModelAdmin):
    #en las tuplas los elementos
    #no son modificables
    list_display = ('nombre_mascota', 'raza', 'Estado')
    #agregaremos una caja de busqueda
    search_fields = ['nombre_mascota', 'raza']

admin.site.register(Raza)
admin.site.register(Mascotas, MascotaAdmin)