# Generated by Django 3.0.7 on 2020-09-17 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['day']},
        ),
        migrations.AlterField(
            model_name='course',
            name='day',
            field=models.IntegerField(),
        ),
    ]
