from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor as S
from .models import Sensor_time_value as ST
from .models import raster_data as R
import json
from django.core.serializers.json import DjangoJSONEncoder

def map_homepage(request):
    context = {
        'timeData': ST.objects.all(),
        'sensor_objects': S.objects.all(),
        'rasterObjects': R.objects.all()
    }
    return render(request, 'map.html', context)

def about(request):
    return render(request, 'about.html')

def map_simulation(request):
    context = {
        'timeData': ST.objects.all(),
        'sensor_objects': S.objects.all(),
        'rasterObjects': R.objects.all()
    }
    return render(request, 'map_sim.html', context)

def current(request):
    context = {
        'timeData': ST.objects.all(),
        'sensor_objects': S.objects.all(),
    }
    return render(request, 'current.html', context)