from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from apps.course.models import Score
from utils import restful, pages
from .models import Superpower

User = get_user_model()


class StudentsListView(View):
    def get(self, request):
        school = request.user.school
        levels = Superpower.objects.all()
        if school:
            current_num = request.GET.get('p', 1)  # 当前页码
            name = request.GET.get('name')
            students = User.objects.select_related('superpower').filter(school=school, is_director=0)

            if name:
                students = students.filter(username__icontains=name)

            paginator = Paginator(students, settings.ONE_PAGE_STUDENTS_LIST_COUNT)  # 每页数据数量
            page_obj = paginator.page(current_num)

            context = {
                'students': page_obj.object_list,  # 获取当前页的数据
                'name': name,
                'paginator': paginator,
                'page_obj': page_obj,
                'levels': levels,
            }

            context_data = self.get_paginator_data(paginator, page_obj)
            context.update(context_data)

            return render(request, 'students/students_list.html', context=context)
        else:
            raise Http404

    def post(self, request):
        student_id = request.POST.get('student_id')
        level_id = request.POST.get('level_id')
        superpower = Superpower.objects.get(pk=level_id)
        student = User.objects.get(uid=student_id)
        student.superpower = superpower
        student.save()
        return restful.ok()

    # 获取当前页码和前后四个页码
    @staticmethod
    def get_paginator_data(paginator, page_obj, around_num=2):
        return pages.pages_process(paginator, page_obj, around_num)


@require_POST
def del_student(request):
    student_id = request.POST.get('student_id')
    user = User.objects.get(pk=student_id)
    user.school = None
    user.save()
    return restful.ok()


def student_score(request):
    scores = Score.objects.select_related('course').filter(student=request.user)
    context = {
        'scores': scores
    }
    return render(request, 'students/student_score.html', context=context)
