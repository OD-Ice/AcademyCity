# Generated by Django 3.0.7 on 2020-09-15 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200914_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='superpower',
            options={'ordering': ['priority']},
        ),
    ]
