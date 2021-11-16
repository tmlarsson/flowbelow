from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Sensor
from .models import Sensor_time_value
from .models import raster_data



class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id_tag','masl')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),
                    path('upload-timedata/', self.upload_timedata),
                    path('upload-rasterdata/', self.upload_rasterdata)
        ]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            firstline = True

            for x in csv_data:
                if firstline:
                    firstline = False
                    continue
                fields = x.split(";")
                created = Sensor.objects.update_or_create(
                    id_tag=fields[2],
                    placement=fields[4],
                    x_cord = fields[6],
                    y_cord = fields[7],
                    sensor_type = fields[3],
                    masl = fields[5],
                    ref_system = fields[8]
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/upload_sensors.html", data)

    def upload_timedata(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            firstline = True

            for x in csv_data:
                if firstline:
                    firstline = False
                    continue
                fields = x.split(";")
                created = Sensor_time_value.objects.update_or_create(
                    row_id = fields[0]+fields[1],
                    id_tag = fields[0],
                    time = fields[1],
                    masl = fields[2],
                    placement = fields[3],
                    data_type = fields[4],
                    filtered = fields[5],
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/upload_timedata.html", data)

    def upload_rasterdata(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            firstline = True

            for x in csv_data:
                if firstline:
                    firstline = False
                    continue
                fields = x.split(";")
                created = Sensor_time_value.objects.update_or_create(
                    id_tag = fields[0],
                    masl = fields[1],
                    ref_system = fields[3],
                    raster = fields[4],
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/upload_rasterdata.html", data)

# Register all models in the Admin page
admin.site.register(Sensor, CustomerAdmin)
admin.site.register(Sensor_time_value, CustomerAdmin)
admin.site.register(raster_data, CustomerAdmin)