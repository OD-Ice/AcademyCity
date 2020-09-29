from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from shortuuidfield import ShortUUIDField
from apps.index.models import School
from django.conf import settings
from apps.student.models import Superpower


class UserManager(BaseUserManager):
    def _create_user(self, telephone, email, username, password, **kwargs):
        if not telephone:
            raise ValueError('请输入手机号码！')
        if not email:
            raise ValueError('请输入邮箱！')
        if not username:
            raise ValueError('请输入用户名!')
        if not password:
            raise ValueError('请输入密码!')

        user = self.model(telephone=telephone, email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, email, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone, email, username, password, **kwargs)

    def create_superuser(self, telephone, email, username, password, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone, email, username, password, **kwargs)


def get_superpower_default_id():
    default = 7
    return default


class User(AbstractUser):
    # 不使用默认的自增长的主键
    # 使用shortuuid
    # Shortuuidfield
    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True)
    avatar = models.URLField(default=settings.DEFAULT_USER_AVATAR)
    superpower = models.ForeignKey(Superpower, on_delete=models.DO_NOTHING, default=get_superpower_default_id)
    is_director = models.BooleanField(default=False)

    USERNAME_FIELD = 'telephone'
    # telephone, username, password
    REQUIRED_FIELDS = ['username', 'email']  # 当通过createsuperuser管理命令创建一个用户时，用于提示的一个字段名称列表
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
