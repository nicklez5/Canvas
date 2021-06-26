from django.urls import path, include , re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
urlpatterns = [
    path('list/',views.StudentList.as_view())
]