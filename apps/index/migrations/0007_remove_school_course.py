# Generated by Django 3.0.7 on 2020-09-15 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20200914_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='course',
        ),
    ]
