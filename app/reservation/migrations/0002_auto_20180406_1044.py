# Generated by Django 2.0.3 on 2018-04-06 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentvisitpage',
            name='travel_Schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Travel_Information'),
        ),
    ]
