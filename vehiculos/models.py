from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

######################################################################################################
class ubicacion(models.Model):
    
    Zona = models.CharField(max_length=50)

    CodigoPostal = models.CharField(max_length=5)

    Lugar = models.CharField(max_length=30, blank=True, null=True)

    Hora = models.CharField(max_length=30, blank=True, null=True)
## el siguiente comando sirve para que no te aparezca el object en lugar del nombre 
    def __str__(self):
        return self.Zona
#el return debe contener alguna clave de la que se esta haciendo la llave foranea
    def get_absolute_url(self):
        return reverse('ubicacion_detalle', args=[str(self.id)])


######################################################################################################
class vehiculos(models.Model):
    Marca = models.CharField(max_length=25)
    Nombre = models.CharField(max_length=25)
    Color =models.CharField(max_length=25)
    Año = models.PositiveIntegerField(null = True, blank = True)
    Disponible = models.CharField(max_length=2)
    Precio = models.PositiveIntegerField(null = True, blank = True)
    portada = models.ImageField(upload_to = 'portada/', blank = True)#esto es unicamente para imagenes 

    Ubicacion = models.ForeignKey(
        ubicacion,
        on_delete=models.CASCADE,
    )
    def __str__(self): 
        return self.Marca[:15]

    def get_absolute_url(self):
        return reverse('vehiculos_detalle', args=[str(self.id)])

    class Meta:
        permissions = [
            ('admin_generic', 'Puede Editar y Crear Vehiculos'),
            ('suscriptor', 'Solo mostrara el detalle')
            ]
   



######################################################################################################
class entregas(models.Model):
    Fecha = models.DateTimeField(auto_now_add=True)
    Serie = models.CharField(max_length=10)
    Cliente = models.CharField(max_length=30)
    Entrega = models.CharField(max_length=30, blank=True, null=True)
    LugarEntrega = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return self.Cliente[:10]
    
    def get_absolute_url(self):
        return reverse('entregas_detalle', args=[str(self.id)])


    class Meta:
        permissions = [
            ('admin_generic_entregas', 'Puede Editar y Crear Vehiculos'),
            ('suscriptor', 'Solo mostrara el detalle')
            ]


######################################################################################################
class almacen(models.Model):
    NumeroSerie = models.CharField(max_length=14)
    Modelo = models.CharField(max_length=14, blank=True, null=True)
    Lote = models.CharField(max_length=3)
    NumAlmacen = models.CharField(max_length=14, blank=True, null=True)
    Fecha = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.NumeroSerie[:15]
    
    def get_absolute_url(self):
        return reverse('almacen_detalle', args=[str(self.id)])

    class Meta:
        permissions = [
            ('admin_generic_almacen', 'Puede Editar y Crear Vehiculos'),
            ('suscriptor', 'Solo mostrara el detalle')
            ]

######################################################################################################

class Comentario(models.Model):
    vehiculos = models.ForeignKey(
        vehiculos,
        on_delete=models.CASCADE,
        related_name='comentarios',

    )
    comentario = models.TextField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('vehiculos')


######################################################################################################
class Comentarioentregas(models.Model):
    entregas = models.ForeignKey(
        entregas,
        on_delete=models.CASCADE,
        related_name='comentarios_entregas',

    )
    comentario = models.TextField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('entregas')



######################################################################################################
class Comentarioalmacen(models.Model):
    almacen = models.ForeignKey(
        almacen,
        on_delete=models.CASCADE,
        related_name='comentarios_almacen',

    )
    comentario = models.TextField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('almacen')