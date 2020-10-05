from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('school_list/', views.SchoolList.as_view(), name='school_list'),
    path('school_level/', views.school_level_view, name='school_level'),
    path('add_school/', views.AddSchool.as_view(), name='add_school'),
    path('edit_school/', views.EditSchool.as_view(), name='edit_school'),
    path('del_school/', views.del_school, name='del_school'),
    path('school_detail/<int:school_id>', views.school_detail, name='school_detail'),
    path('add_school_level/', views.add_school_level, name='add_school_level'),
    path('edit_school_level/', views.edit_school_level, name='edit_school_level'),
    path('del_school_level/', views.del_school_level, name='del_school_level'),
    path('upload_badge/', views.upload_badge_view, name='upload_badge'),
    path('join_school/', views.join_school_view, name='join_school'),
    path('quit_school/', views.quit_school_view, name='quit_school'),
    path('add_comment/', views.add_comment_view, name='add_comment_view'),
    path('director_list/', views.DirectorList.as_view(), name='director_list'),
    path('del_director/', views.del_director, name='del_director'),
    path('add_message/', views.add_message, name='add_message'),
    path('agree_apply_level/', views.agree_apply_level, name='agree_apply_level'),
    path('agree_apply_director/', views.agree_apply_director, name='agree_apply_director'),
    path('del_message/', views.del_message, name='del_message'),
]
