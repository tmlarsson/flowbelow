from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sensors', views.sensor_list_view),
]
