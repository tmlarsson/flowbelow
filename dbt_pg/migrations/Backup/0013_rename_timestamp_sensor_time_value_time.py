# Generated by Django 3.2.9 on 2021-11-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbt_pg', '0012_rename_time_sensor_time_value_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor_time_value',
            old_name='timestamp',
            new_name='time',
        ),
    ]
