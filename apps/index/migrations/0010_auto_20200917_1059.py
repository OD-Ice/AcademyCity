# Generated by Django 3.0.7 on 2020-09-17 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20200917_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['school_level'], 'permissions': [('fire_student', '开除学生'), ('fire_director', '开除校级管理者')]},
        ),
    ]
