# Generated by Django 4.0.3 on 2022-04-18 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_project_project_landingpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_landingpage',
            field=models.ImageField(upload_to='media/'),
        ),
    ]