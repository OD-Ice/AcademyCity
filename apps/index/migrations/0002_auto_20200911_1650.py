# Generated by Django 3.0.7 on 2020-09-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoollevel',
            name='priority',
            field=models.IntegerField(unique=True),
        ),
    ]
