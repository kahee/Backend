# Generated by Django 2.0.3 on 2018-04-23 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelinformation',
            old_name='price_descrption',
            new_name='price_description',
        ),
    ]