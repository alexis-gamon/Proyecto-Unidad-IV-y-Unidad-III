from django.contrib import admin
from .models import Ubicacion, vehiculos, entregas, almacen, Comentario

# Register your models here.

admin.site.register(vehiculos)
admin.site.register(Ubicacion)
admin.site.register(entregas)
admin.site.register(almacen)
admin.site.register(Comentario) 

#class ComentarioInline(admin.StackedInline):
#    model = Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario


        


