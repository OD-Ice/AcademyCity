from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('publish_course/', views.publish_course_view, name='publish_course'),
    path('select_school_course/', views.select_school_course, name='select_school_course'),
    path('add_course/', views.add_course, name='add_course'),
    path('time_table/', views.TimeTable.as_view(), name='time_table'),
    path('select_course/', views.select_course, name='select_course'),
    path('submit_event/', views.submit_event, name='submit_event'),
    path('course_list/<school_id>/', views.course_list_view, name='course_list'),
    path('course_score/<course_id>/', views.CourseScoreView.as_view(), name='course_score'),
]
