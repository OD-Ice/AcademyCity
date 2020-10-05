from django.db import models
from picklefield.fields import PickledObjectField


class SchoolCategory(models.Model):
    name = models.CharField(max_length=10)


class SchoolLevel(models.Model):
    name = models.CharField(max_length=10)
    priority = models.IntegerField(unique=True)

    class Meta:
        ordering = ['priority']


class School(models.Model):
    name = models.CharField(max_length=20, error_messages={'required': '请输入学校名称！'})
    school_level = models.ForeignKey('SchoolLevel', on_delete=models.SET_NULL, null=True)
    school_category = models.ForeignKey('SchoolCategory', on_delete=models.SET_NULL, null=True)
    is_super = models.BooleanField()
    school_badge = models.URLField(error_messages={'required': '请传入学校校徽！'})
    location = models.CharField(max_length=50, error_messages={'required': '请输入学校地址！'})
    email = models.EmailField(error_messages={'required': '请输入学校邮箱！'})
    course_des = models.TextField(null=True, error_messages={'required': '请输入主教课程！'})
    desc = models.TextField(error_messages={'required': '请输入学校描述！'})
    reg_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['school_level']
        permissions = [
            ('fire_student', '开除学生'),
            ('fire_director', '开除校级管理者'),
        ]


class Comments(models.Model):
    content = models.TextField(max_length=300)
    author = models.ForeignKey('acauth.User', on_delete=models.SET_NULL, null=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-pub_time']


class TodoListType(models.Model):
    name = models.CharField(max_length=20)


class TodoList(models.Model):
    content = models.CharField(max_length=100)
    type = models.ForeignKey('TodoListType', on_delete=models.DO_NOTHING, null=True)
    sponsor = models.ForeignKey('acauth.User', on_delete=models.DO_NOTHING, null=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    data = PickledObjectField(null=True)

    class Meta:
        ordering = ['-pub_time']
