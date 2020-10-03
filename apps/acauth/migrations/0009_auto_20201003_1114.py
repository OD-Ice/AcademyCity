# Generated by Django 3.0.7 on 2020-10-03 03:14

import apps.acauth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200915_1639'),
        ('acauth', '0008_auto_20200918_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='superpower',
            field=models.ForeignKey(default=apps.acauth.models.get_superpower_default_id, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_set', to='student.Superpower'),
        ),
    ]
