from django.urls import path
from . import views

app_name = 'tiny'

urlpatterns = [
    path('upload/', views.upload_view, name='upload')
]