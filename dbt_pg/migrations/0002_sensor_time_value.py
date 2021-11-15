# Generated by Django 3.2.9 on 2021-11-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbt_pg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_time_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tag', models.CharField(default='123ABC', max_length=100)),
                ('time', models.DateTimeField()),
                ('masl', models.CharField(default='', max_length=20)),
                ('placement', models.CharField(default='', max_length=100)),
                ('data_type', models.CharField(default='', max_length=20)),
                ('filtered', models.BooleanField(default='', max_length=20)),
            ],
        ),
    ]
