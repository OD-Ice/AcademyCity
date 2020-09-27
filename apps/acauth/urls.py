from django.urls import path
from . import views

app_name = 'acauth'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('img_captcha/', views.image_captcha, name='img_captcha'),
    # path('operate_group/', views.operate_group, name='operate_group'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'),
]
