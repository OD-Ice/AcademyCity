# Generated by Django 3.0.7 on 2020-09-18 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acauth', '0007_auto_20200918_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
