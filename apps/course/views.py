import json
from django.shortcuts import render
from django.views.decorators.http import require_POST
from utils import restful
from .models import Course, WeekDay, CourseTime, Score
from apps.index.models import School
from django.http import Http404
from django.views import View
from .serializers import CourseSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


def publish_course_view(request):
    school = request.user.school
    if school:
        courses = Course.objects.select_related('week_day', 'course_time').all()
        weekdays = WeekDay.objects.all()
        course_times = CourseTime.objects.all()
        context = {
            'courses': courses,
            'weekdays': weekdays,
            'course_times': course_times,
        }
        return render(request, 'course/publish_course.html', context=context)
    else:
        raise Http404


@require_POST
def select_school_course(request):
    school_id = request.POST.get('school_id')
    course_ids = json.loads(request.POST.get('course_ids'))
    school = School.objects.get(pk=school_id)
    school.course_set.set(course_ids)
    school.save()
    return restful.ok()


@require_POST
def add_course(request):
    name = request.POST.get('course_name')
    week_day_id = request.POST.get('week_day_id')
    course_time_id = request.POST.get('course_time_id')
    week_day = WeekDay.objects.get(pk=week_day_id)
    course_time = CourseTime.objects.get(pk=course_time_id)
    course = Course.objects.create(name=name, week_day=week_day, course_time=course_time)
    return restful.result(code=200, data={
        'week_day': week_day.name,
        'course_time': course_time.name,
        'id': course.pk,
    })


class TimeTable(View):
    def get(self, request):
        user = request.user
        school = user.school
        school_courses = school.course_set.all()
        user_courses = user.course_set.all()
        course_times = CourseTime.objects.all()
        mon = []
        tue = []
        wed = []
        thu = []
        fri = []
        weeks = [mon, tue, wed, thu, fri]
        course_type = []
        for i in weeks:
            for j in range(1, 5):
                try:
                    i.append(user_courses.filter(week_day_id=weeks.index(i)+1).filter(course_time_id=j).first().name)
                except:
                    i.append('')
        weeks = json.dumps(weeks)
        for course_time in course_times:
            course_type.append([{'index': course_time.pk, 'name': course_time.name}, 1])
        course_type = json.dumps(course_type)
        context = {
            'user_courses': user_courses,
            'school_courses': school_courses,
            'weeks': weeks,
            'course_type': course_type,
        }
        return render(request, 'course/time_table.html', context=context)


@require_POST
def select_course(request):
    school = request.user.school
    school_courses = school.course_set.all()
    week = request.POST.get('week')  # 周几
    index = request.POST.get('index')  # 第几节课
    week_day = WeekDay.objects.get(name=week)
    course_time = CourseTime.objects.get(pk=index)
    current_courses = school_courses.filter(week_day=week_day, course_time=course_time)
    serializer = CourseSerializer(current_courses, many=True)
    return restful.result(data=serializer.data)


@require_POST
def submit_event(request):
    course_id = int(request.POST.get('course_id'))
    week_name = request.POST.get('week')
    course_time = request.POST.get('course_time')
    week_day = WeekDay.objects.get(name=week_name)
    course_time = CourseTime.objects.get(pk=course_time)
    if course_id != 0:
        course = Course.objects.get(pk=course_id)
        Score.objects.filter(course__week_day=week_day, course__course_time=course_time, student=request.user).delete()
        Score.objects.create(student=request.user, course=course)
    else:
        Score.objects.filter(course__week_day=week_day, course__course_time=course_time, student=request.user).delete()
    return restful.ok()


def course_list_view(request, school_id):
    school = School.objects.get(pk=school_id)
    courses = Course.objects.filter(school=school)
    context = {
        'courses': courses
    }
    return render(request, 'course/course_list.html', context=context)


class CourseScoreView(View):
    def get(self, request, course_id):
        school = request.user.school
        course = Course.objects.get(pk=course_id)
        students = User.objects.filter(school=school, course=course)
        scores = Score.objects.select_related('student').filter(student__in=students, course=course)
        context = {
            'scores': scores,
            'course': course,
        }
        return render(request, 'course/course_score.html', context=context)

    def post(self, request, course_id):
        student_id = request.POST.get('studentId')
        student = User.objects.get(pk=student_id)
        course = Course.objects.get(pk=course_id)
        score = request.POST.get('score')
        Score.objects.filter(student=student, course=course).update(score=score)
        return restful.ok()
