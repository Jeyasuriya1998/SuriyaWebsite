# Generated by Django 3.0.3 on 2020-08-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0002_auto_20200813_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='thumbnil',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='thumbnil',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
