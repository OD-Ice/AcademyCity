from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('student_list/', views.StudentsListView.as_view(), name='student_list'),
    path('del_student_school/', views.del_student, name='del_student_school'),
    path('student_score/', views.student_score, name='student_score'),
]