# Generated by Django 3.0.7 on 2020-09-11 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('is_super', models.BooleanField()),
                ('school_badge', models.URLField()),
                ('location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('school_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.SchoolCategory')),
                ('school_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.SchoolLevel')),
            ],
        ),
    ]
