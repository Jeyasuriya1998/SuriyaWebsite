# Generated by Django 3.0.3 on 2020-08-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsiteapp', '0003_auto_20200814_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf'),
        ),
        migrations.AddField(
            model_name='projects',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf'),
        ),
    ]
