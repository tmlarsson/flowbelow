from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_homepage, name='Homepage'),
    path('about', views.about, name='About us'),
    path('simulations', views.map_simulation, name='Simulations'),
    path('current', views.current, name='Timeseries')
]
