from django.db import models

# Create your models here.
class Sensor(models.Model):
    id_tag = models.CharField(max_length=100, default='123ABC')
    placement = models.CharField(max_length=200, default='Träbro')
    area = models.CharField(max_length=200, default='Mariehem')
    city = models.CharField(max_length=100, default='Umeå')
    x_cord = models.CharField(max_length=40, default='')
    y_cord = models.CharField(max_length=40, default='')
    masl = models.CharField(max_length=20, default='')
    sensor_type = models.CharField(max_length=40,default='')
    ref_system = models.CharField(max_length=20,default='')
    has_simulations = models.BooleanField(max_length=200,default=False)
    simul_path = models.CharField(max_length=200,default='')