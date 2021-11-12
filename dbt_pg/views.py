from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor

def sensor_list_view(request):
    sensor_objects = Sensor.objects.all()
    context = {
        'sensor_objects': sensor_objects
    }
    return render(request, 'list_sensors.html', context)

def index(request):
    return render(request, 'homepage.html')

