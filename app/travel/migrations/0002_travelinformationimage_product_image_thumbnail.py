# Generated by Django 2.0.3 on 2018-04-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelinformationimage',
            name='product_image_thumbnail',
            field=models.ImageField(default=1, upload_to='product-thumbnail'),
            preserve_default=False,
        ),
    ]