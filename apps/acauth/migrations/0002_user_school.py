# Generated by Django 3.0.7 on 2020-09-14 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20200913_1320'),
        ('acauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='index.School'),
        ),
    ]
