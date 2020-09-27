from django.db import models


class WeekDay(models.Model):
    name = models.CharField(max_length=4)


class CourseTime(models.Model):
    name = models.CharField(max_length=50)


class Course(models.Model):
    name = models.CharField(max_length=20)
    week_day = models.ForeignKey('WeekDay', on_delete=models.DO_NOTHING, null=True)
    course_time = models.ForeignKey('CourseTime', on_delete=models.DO_NOTHING, null=True)
    school = models.ManyToManyField('index.School')
    student = models.ManyToManyField('acauth.User', through='Score')

    class Meta:
        ordering = ['week_day', 'course_time']


class Score(models.Model):
    student = models.ForeignKey('acauth.User', on_delete=models.DO_NOTHING)
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING)
    score = models.FloatField(null=True)
