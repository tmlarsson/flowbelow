from django.urls import path
from . import views

urlpatterns = [
    path('sensors', views.sensor_list_view),
    path('timedata', views.plot_timedata, name='Timeseries'),
    path('view_timedata', views.view_timedata, name='Timeseries'),
    path('', views.map_homepage, name='Homepage'),
]
