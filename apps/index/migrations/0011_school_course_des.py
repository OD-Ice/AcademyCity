# Generated by Django 3.0.7 on 2020-09-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20200917_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='course_des',
            field=models.TextField(null=True),
        ),
    ]
