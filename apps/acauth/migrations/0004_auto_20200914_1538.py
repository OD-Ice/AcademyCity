# Generated by Django 3.0.7 on 2020-09-14 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('acauth', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_director',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='superpower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Superpower'),
        ),
    ]
