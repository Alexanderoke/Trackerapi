# Generated by Django 4.0.3 on 2022-04-18 14:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_project_project_landingpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_landingpage',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
