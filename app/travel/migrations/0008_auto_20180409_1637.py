# Generated by Django 2.0.3 on 2018-04-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_auto_20180409_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelschedule',
            name='maxPeople',
        ),
        migrations.RemoveField(
            model_name='travelschedule',
            name='price',
        ),
        migrations.RemoveField(
            model_name='travelschedule',
            name='price_descrption',
        ),
        migrations.AddField(
            model_name='travelinformation',
            name='maxPeople',
            field=models.IntegerField(default=1, verbose_name='최대 사람 수'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travelinformation',
            name='price',
            field=models.IntegerField(default=0, verbose_name='상품금액'),
        ),
        migrations.AddField(
            model_name='travelinformation',
            name='price_descrption',
            field=models.TextField(default=1, verbose_name='상품금액 포함사항'),
            preserve_default=False,
        ),
    ]