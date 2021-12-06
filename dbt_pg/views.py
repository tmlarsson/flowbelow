from django.shortcuts import render
from .models import Sensor as S
from .models import Sensor_time_value as ST
from .models import raster_data as R
import datetime

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
        'rasterObjects': R.objects.all(),
        'timesUsed': ST.objects.values('time').distinct().order_by('time')
    }
    return render(request, 'map_sim.html', context)