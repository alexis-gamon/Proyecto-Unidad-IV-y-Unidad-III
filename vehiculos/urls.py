

from .views import ResultadoBusqueda2ListView, homeTemplateView, vehiculosTemplateView, entregasTemplateView, almacenTemplateView, vehiculosPageDetail, vehiculosPagesCreate, vehiculosPageUpdate, vehiculosPageDelete, ComentariosCreateView, ComentariosDeleteView, entregasPageDetail, entregasPagesCreate, entregasPageUpdate, entregasPageDelete, almacenPageDetail, almacenPagesCreate, almacenPageUpdate, almacenPageDelete, ubicacionTemplateView, ubicacionPageDetail, ubicacionPagesCreate, ubicacionPageUpdate, ubicacionPageDelete, ResultadoBusquedaListView, ComentarioentregasCreateView, ComentariosentregasDeleteView, ComentariosalmacenCreateView, ComentariosalmacenDeleteView
from django.urls import path

urlpatterns = [
    path('',homeTemplateView.as_view(), name='home'),
    path('vehiculos/',vehiculosTemplateView.as_view(), name='vehiculos'),
    path('entregas/',entregasTemplateView.as_view(), name='entregas'),
    path('/almacen/',almacenTemplateView.as_view(), name='almacen'),
    path('/ubicacion/',ubicacionTemplateView.as_view(), name='ubicacion'),
    

    ####################        VEHICULOS    #############################################

### Detalle
    path('vehiculos/<int:pk>/', vehiculosPageDetail.as_view(), name='vehiculos_detalle'),
### Crear
    path('vehiculos/nuevo/', vehiculosPagesCreate.as_view(), name="vehiculos_nuevo"),
### Modificar
    path('vehiculos/<int:pk>/editar/', vehiculosPageUpdate.as_view(), name="vehiculos_editar"),

### Borrar 
    path('vehiculos/<int:pk>/eliminar/', vehiculosPageDelete.as_view(), name="vehiculos_eliminar"),

### Comentario
    path('<int:pk>/Comentario/',ComentariosCreateView.as_view(), name='Comentario'),

    path('vehiculos/<int:pk>/Comentario_eliminar/',ComentariosDeleteView.as_view(), name='Comentario_eliminar'),


####################        ENTREGAS    #############################################


### Detalle
    path('entregas/<int:pk>/', entregasPageDetail.as_view(), name='entregas_detalle'),
### Crear
    path('entregas/nuevo/', entregasPagesCreate.as_view(), name="entregas_nuevo"),
### Modificar
    path('entregas/<int:pk>/editar/', entregasPageUpdate.as_view(), name="entregas_editar"),

### Borrar 
    path('entregas/<int:pk>/eliminar/', entregasPageDelete.as_view(), name="entregas_eliminar"),

### Comentario
    path('entregas/<int:pk>/Comentario/',ComentarioentregasCreateView.as_view(), name='Comentarioentregas'),

    path('entregas/<int:pk>/Comentario_eliminar/',ComentariosentregasDeleteView.as_view(), name='Comentario_eliminar_entregas'),

####################        ALMACEN    #############################################

### Detalle
    path('almacen/<int:pk>/', almacenPageDetail.as_view(), name='almacen_detalle'),
### Crear
    path('almacen/nuevo/', almacenPagesCreate.as_view(), name="almacen_nuevo"),
### Modificar
    path('almacen/<int:pk>/editar/', almacenPageUpdate.as_view(), name="almacen_editar"),

### Borrar 
    path('almacen/<int:pk>/eliminar/', almacenPageDelete.as_view(), name="almacen_eliminar"),

### Comentario
    path('almacen/<int:pk>/Comentario/',ComentariosalmacenCreateView.as_view(), name='Comentarioalmacen'),

    path('almacen/<int:pk>/Comentario_eliminar/',ComentariosalmacenDeleteView.as_view(), name='Comentario_eliminar_almacen'),

####################        UBICACION    #############################################

### Detalle
    path('ubicacion/<int:pk>/', ubicacionPageDetail.as_view(), name='ubicacion_detalle'),
### Crear
    path('ubicacion/nuevo/', ubicacionPagesCreate.as_view(), name="ubicacion_nuevo"),
### Modificar
    path('ubicacion/<int:pk>/editar/', ubicacionPageUpdate.as_view(), name="ubicacion_editar"),

### Borrar 
    path('ubicacion/<int:pk>/eliminar/', ubicacionPageDelete.as_view(), name="ubicacion_eliminar"),

########################### Busqueda##############################################################


##aqui se hizo un cambio
    path('busquedaVehiculo/',ResultadoBusquedaListView.as_view(), name="resul_busqueda"),
    path('<int:pk>/busquedaalmacen/',ResultadoBusqueda2ListView.as_view(), name="resul_busqueda2"),

    

]