# Generated by Django 3.2.4 on 2021-12-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211104_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='delivery_phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]