# Generated by Django 3.0.7 on 2020-09-14 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.School'),
        ),
    ]
