
from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.index, name='index'),
    path('myapp/', include('myapp.urls')),
    
]
