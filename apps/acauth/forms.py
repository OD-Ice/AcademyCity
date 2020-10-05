from django import forms
from apps.forms import FormMixin
from django.core.cache import cache
from .models import User


class LoginForm(forms.Form, FormMixin):
    telephone = forms.CharField(max_length=11, min_length=11)
    password = forms.CharField(max_length=20, min_length=6, error_messages={'max_length': '密码最多不能超过20个字符!', 'min_length': '密码最少为6位！'})
    remember = forms.BooleanField(required=False)


class RegisterForm(forms.Form, FormMixin):
    username = forms.CharField(max_length=20)
    telephone = forms.CharField(max_length=11, min_length=11)
    email = forms.EmailField()
    password1 = forms.CharField(min_length=6, max_length=20, error_messages={'max_length': '密码最多不能超过20个字符!', 'min_length': '密码最少为6位！'})
    password2 = forms.CharField(min_length=6, max_length=20,error_messages={'max_length': '密码最多不能超过20个字符!', 'min_length': '密码最少为6位！'})
    img_captcha = forms.CharField(min_length=4, max_length=4)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('两次密码输入不一致！')

        img_captcha = cleaned_data.get('img_captcha')
        if img_captcha:
            cached_img_captcha = cache.get(img_captcha.lower())
            if not cached_img_captcha or cached_img_captcha.lower() != img_captcha.lower():
                raise forms.ValidationError('图形验证码错误！')

        telephone = cleaned_data.get('telephone')
        tel_exists = User.objects.filter(telephone=telephone).exists()
        if tel_exists:
            raise forms.ValidationError('该手机号码已注册！')

        email = cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise forms.ValidationError('该邮箱已注册！')
