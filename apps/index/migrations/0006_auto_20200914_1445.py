# Generated by Django 3.0.7 on 2020-09-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_comments_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(max_length=300),
        ),
    ]
