# Generated by Django 3.0.7 on 2020-09-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_school_course_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='course_des',
            field=models.TextField(error_messages={'required': '请输入主教课程！'}, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='desc',
            field=models.TextField(error_messages={'required': '请输入学校描述！'}),
        ),
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.EmailField(error_messages={'required': '请输入学校邮箱！'}, max_length=254),
        ),
        migrations.AlterField(
            model_name='school',
            name='location',
            field=models.CharField(error_messages={'required': '请输入学校地址！'}, max_length=50),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(error_messages={'required': '请输入学校名称！'}, max_length=20),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_badge',
            field=models.URLField(error_messages={'required': '请传入学校校徽！'}),
        ),
    ]
