from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_simulation, name='Homepage'),
    path('about', views.about, name='About us'),
]
