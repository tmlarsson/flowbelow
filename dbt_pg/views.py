from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor as S
from .models import Sensor_time_value as ST

def sensor_list_view(request):
    sensor_objects = S.objects.all()
    context = {
        'sensor_objects': sensor_objects
    }
    return render(request, 'list_sensors.html', context)

def index(request):
    return render(request, 'map.html')

def plot_timedata(request):
    context = {
        'timeData': ST.objects.all().filter(id_tag='A81758FFFE045989')
    }
    return render(request, 'timedata.html', context)

def view_timedata(request):
    timedata = ST.objects.all().filter(id_tag='A81758FFFE045989')
    context = {
        'timedata': timedata
    }
    return render(request, 'list_timedata.html', context)

def map(request):
    timedata = ST.objects.all().filter(id_tag='A81758FFFE045989')
    context = {
        'timeData': timedata
    }
    return render(request, 'map.html', context)