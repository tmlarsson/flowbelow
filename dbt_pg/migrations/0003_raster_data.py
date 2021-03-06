# Generated by Django 3.2.9 on 2021-11-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbt_pg', '0002_delete_raster_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='raster_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tag', models.CharField(default='', max_length=20)),
                ('masl', models.CharField(default=0, max_length=10)),
                ('ref_system', models.CharField(default='', max_length=20)),
                ('img', models.CharField(default='', max_length=100)),
                ('tr', models.CharField(default='', max_length=20)),
                ('bl', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
