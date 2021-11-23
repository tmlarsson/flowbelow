from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sensors', views.sensor_list_view),
    path('timedata', views.plot_timedata, name='Timeseries'),
    path('view_timedata', views.view_timedata, name='Timeseries'),
    path('map', views.map, name='map'),
]
