

from django.urls import path
from webtest.views import index, nosotros, productos, contacto, detalle_producto


urlpatterns = [
    
    path('', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),  
    path('productos/', productos, name='productos'),
    path('contacto/', contacto, name='contacto'), 
     path('productos/<int:pk>/', detalle_producto, name='detalle_producto'),     
]
