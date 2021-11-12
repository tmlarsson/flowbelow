from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Sensor



class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id_tag','placement')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
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
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Sensor, CustomerAdmin)