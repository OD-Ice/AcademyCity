import os
from urllib import parse
from django.conf import settings
from django.contrib.auth.models import Group, Permission, ContentType
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm, RegisterForm
from utils import restful
from io import BytesIO
from utils.captcha.accaptcha import Captcha
from django.core.cache import cache
from django.contrib.auth import get_user_model
from apps.index.models import School, SchoolLevel
from apps.course.models import Score, Course

User = get_user_model()


class Login(View):
    def get(self, request):
        if not hasattr(request, 'user') or not request.user.is_authenticated:
            return render(request, 'acauth/login.html')
        else:
            return redirect(reverse('index:index'))

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request, telephone=telephone, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if remember:
                        request.session.set_expiry(None)
                    else:
                        request.session.set_expiry(0)
                    return restful.ok()
                else:
                    return restful.unauth('您的账号已被冻结！')
            else:
                return restful.params_error('用户名或密码错误！')
        else:
            return restful.params_error(form.get_errors())


class Register(View):
    def get(self, request):
        if not hasattr(request, 'user') or not request.user.is_authenticated:
            return render(request, 'acauth/register.html')
        else:
            return redirect(reverse('index:index'))

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username, telephone=telephone, email=email, password=password)
            login(request, user)
            return restful.ok()
        else:
            return restful.params_error(form.get_errors())


def image_captcha(request):
    text, image = Captcha.gene_code()
    # BytesIO：相当于一个管道，用来存储图片的数据流
    out = BytesIO()
    # 调用image的save方法，将图片存储到BytesIO中
    image.save(out, 'png')
    # 将BytesIO文件的指针移动到最开始的位置
    out.seek(0)

    response = HttpResponse(content_type='image/png')
    # 从BytesIO的管道中，读取出图片数据，保存到response对象上
    response.write(out.read())
    # 文件指针跑到了最后面，tell()方法指出指针的位置，即文件的大小
    response['Content-length'] = out.tell()
    # 将验证码保存在缓存中
    cache.set(text.lower(), text.lower(), 5 * 60)

    return response


# 操作分组
# def operate_group(request):
#     # Group.objects.create(name='学生')
#     # group = Group.objects.filter(name='校级管理者').first()
#     # content_type = ContentType.objects.get_for_model(Score)
#     # permissions = Permission.objects.filter(content_type=content_type)
#     # group.permissions.set(permissions)
#     # group.save()
#     return HttpResponse('添加成功！')

@require_POST
def upload_avatar(request):
    file = request.FILES.get('file')
    print(file)
    name = file.name
    with open(os.path.join(settings.MEDIA_ROOT, name), 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = parse.unquote(request.build_absolute_uri(settings.MEDIA_URL + name))
    request.user.avatar = url
    request.user.save()
    return restful.ok()
