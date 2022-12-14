from django.urls import path 
from .views import OrdersPageView
from .views import *



urlpatterns = [
    path('<int:pk>/', OrdersPageView.as_view(), name='orders'),
    path('charge/', charge, name='charge'),
    path('<int:pk>/',Ordervehiculos.as_view(), name='pago_vehiculos'),
]
