from django.core.paginator import Paginator
from django.shortcuts import render
from .models import SchoolCategory, SchoolLevel, School, Comments
from django.views.decorators.http import require_POST
from .forms import SchoolLevelForm, SchoolForm
from utils import restful, pages
from django.views import View
from urllib import parse
import os
from django.conf import settings
from django.http import Http404
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return render(request, 'index/index.html')


@require_POST
def add_school_level(request):
    form = SchoolLevelForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        priority = form.cleaned_data.get('priority')
        SchoolLevel.objects.create(name=name, priority=priority)
        return restful.ok()
    else:
        return restful.params_error(form.get_errors())


@require_POST
def edit_school_level(request):
    form = SchoolLevelForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        priority = form.cleaned_data.get('priority')
        level_id = int(request.POST.get('level_id'))
        try:
            SchoolLevel.objects.get(pk=level_id).update(name=name, priority=priority)
            return restful.ok()
        except:
            return restful.params_error('该科研等级不存在！')
    else:
        return restful.params_error(form.get_errors())


@require_POST
def del_school_level(request):
    level_id = int(request.POST.get('level_id'))
    try:
        SchoolLevel.objects.get(pk=level_id).delete()
        return restful.ok()
    except:
        return restful.params_error('该科研等级不存在！')


def school_level_view(request):
    levels = SchoolLevel.objects.all()
    context = {
        'levels': levels
    }
    return render(request, 'index/school_level.html', context=context)


class SchoolList(View):
    def get(self, request):
        current_num = request.GET.get('p', 1)  # 当前页码
        school = request.GET.get('school')  # 查询的学校关键字
        level_id = int(request.GET.get('level') or 0)  # 查询的研究等级
        category_id = int(request.GET.get('category') or 0)  # 查询的分类
        categories = SchoolCategory.objects.all()
        levels = SchoolLevel.objects.all()
        schools = School.objects.select_related('school_category', 'school_level')

        if school:
            schools = schools.filter(name__icontains=school)
        if level_id and level_id != 0:
            schools = schools.filter(school_level_id=level_id)
        if category_id and category_id != 0:
            schools = schools.filter(school_category_id=category_id)

        paginator = Paginator(schools, settings.ONE_PAGE_SCHOOL_LIST_COUNT)  # 每页两条数据
        page_obj = paginator.page(current_num)

        context = {
            'categories': categories,
            'levels': levels,
            'schools': page_obj.object_list,  # 获取当前页的数据
            'school': school,
            'level_id': level_id,
            'category_id': category_id,
            'paginator': paginator,
            'page_obj': page_obj,
            'url_query': '&' + parse.urlencode({
                'school': school or '',
                'level': level_id or '',
                'category': category_id or '',
            })
        }
        print(type(schools))
        context_data = self.get_paginator_data(paginator, page_obj)
        context.update(context_data)
        return render(request, 'index/school_list.html', context=context)

    # 获取当前页码和前后四个页码
    @staticmethod
    def get_paginator_data(paginator, page_obj, around_num=2):
        return pages.pages_process(paginator, page_obj, around_num)


@require_POST
def upload_badge_view(request):
    file = request.FILES.get('file')
    name = file.name
    with open(os.path.join(settings.MEDIA_ROOT, name), 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = parse.unquote(request.build_absolute_uri(settings.MEDIA_URL+name))
    return restful.result(data={'url': url})


class AddSchool(View):
    def get(self, request):
        categories = SchoolCategory.objects.all()
        levels = SchoolLevel.objects.all()
        context = {
            'categories': categories,
            'levels': levels,
        }
        return render(request, 'index/edit_school.html', context=context)

    def post(self, request):
        form = SchoolForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            exists = School.objects.filter(name=name).exists()
            if exists:
                return restful.params_error('此学校已经注册！')
            else:
                school_level_id = form.cleaned_data.get('school_level')
                print(school_level_id)
                school_category_id = form.cleaned_data.get('school_category')
                is_super = form.cleaned_data.get('is_super')
                school_badge = form.cleaned_data.get('school_badge')
                location = form.cleaned_data.get('location')
                email = form.cleaned_data.get('email')
                course = form.cleaned_data.get('course_des')
                desc = form.cleaned_data.get('desc')
                school_level = SchoolLevel.objects.filter(pk=school_level_id).first()
                school_category = SchoolCategory.objects.filter(pk=school_category_id).first()
                School.objects.create(name=name, school_level=school_level, school_category=school_category, is_super=is_super, school_badge=school_badge, location=location, email=email, course_des=course, desc=desc)
                return restful.ok()
        else:
            return restful.params_error(form.get_errors())


class EditSchool(View):
    def get(self, request):
        school_id = request.GET.get('school_id')
        categories = SchoolCategory.objects.all()
        levels = SchoolLevel.objects.all()
        school = School.objects.select_related('school_category', 'school_level').get(pk=school_id)
        context = {
            'categories': categories,
            'levels': levels,
            'school': school,
        }
        return render(request, 'index/edit_school.html', context=context)

    def post(self, request):
        form = SchoolForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            school_level_id = form.cleaned_data.get('school_level')
            print(school_level_id)
            school_category_id = form.cleaned_data.get('school_category')
            is_super = form.cleaned_data.get('is_super')
            school_badge = form.cleaned_data.get('school_badge')
            location = form.cleaned_data.get('location')
            email = form.cleaned_data.get('email')
            course = form.cleaned_data.get('course_des')
            desc = form.cleaned_data.get('desc')
            school_level = SchoolLevel.objects.filter(pk=school_level_id).first()
            school_category = SchoolCategory.objects.filter(pk=school_category_id).first()
            school_id = request.POST.get('school_id')
            school = School.objects.filter(pk=school_id)
            school.update(name=name, school_level=school_level, school_category=school_category, is_super=is_super, school_badge=school_badge, location=location, email=email, course_des=course, desc=desc)
            return restful.ok()
        else:
            return restful.params_error(form.get_errors())


@require_POST
def del_school(request):
    school_id = int(request.POST.get('school_id'))
    try:
        School.objects.get(pk=school_id).delete()
        return restful.ok()
    except:
        return restful.params_error('该学校不存在！')


def school_detail(request, school_id):
    try:
        school = School.objects.select_related('school_level', 'school_category').get(pk=school_id)
        comments = Comments.objects.select_related('author').filter(school_id=school_id)
        context = {
            'school': school,
            'comments': comments,
        }
        return render(request, 'index/school_detail.html', context=context)
    except:
        return Http404


@require_POST
def join_school_view(request):
    school_id = request.POST.get('school_id')
    school = School.objects.get(pk=school_id)
    user = request.user
    user.school = school
    user.save()
    return restful.ok()


@require_POST
def quit_school_view(request):
    user = request.user
    user.school = None
    user.save()
    return restful.ok()


@require_POST
def add_comment_view(request):
    content = request.POST.get('content')
    school_id = request.POST.get('school_id')
    school = School.objects.get(pk=school_id)
    user = request.user
    Comments.objects.create(content=content, author=user, school=school)
    return restful.ok()


class DirectorList(View):
    def get(self, request):
        current_num = request.GET.get('p', 1)  # 当前页码
        school = int(request.GET.get('school') or 0)  # 查询学校分类
        name = request.GET.get('name')  # 查询管理者姓名
        schools = School.objects.all()
        directors = User.objects.select_related('school', 'superpower').filter(is_director=True)

        if name:
            directors = directors.filter(username__icontains=name)

        if school and school != 0:
            directors = directors.filter(school_id=school)

        paginator = Paginator(directors, settings.ONE_PAGE_DIRECTORS_LIST_COUNT)  # 每页两条数据
        page_obj = paginator.page(current_num)

        context = {
            'directors': page_obj.object_list,  # 获取当前页的数据
            'paginator': paginator,
            'page_obj': page_obj,
            'name': name,
            'schools': schools,
            'school_id': school,
            'url_query': '&' + parse.urlencode({
                'name': name or '',
                'school': school or '',
            })
        }

        context_data = self.get_paginator_data(paginator, page_obj)
        context.update(context_data)

        return render(request, 'index/director_list.html', context=context)

    # 获取当前页码和前后四个页码
    @staticmethod
    def get_paginator_data(paginator, page_obj, around_num=2):
        return pages.pages_process(paginator, page_obj, around_num)


@require_POST
def del_director(request):
    director_id = request.POST.get('director_id')
    user = User.objects.get(pk=director_id)
    user.is_director = 0
    user.save()
    return restful.ok()

