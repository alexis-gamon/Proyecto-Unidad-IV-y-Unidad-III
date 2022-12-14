from django.contrib import admin
from .models import ubicacion, vehiculos, entregas, almacen, Comentario, Comentarioentregas, Comentarioalmacen

# Register your models here.

admin.site.register(vehiculos)
admin.site.register(ubicacion)
admin.site.register(entregas)
admin.site.register(almacen)
admin.site.register(Comentario) 

admin.site.register(Comentarioentregas)
admin.site.register(Comentarioalmacen)
#class ComentarioInline(admin.StackedInline):
#    model = Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario



        


