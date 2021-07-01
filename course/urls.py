from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('courses/',views.CourseList.as_view()),
    path('courses/post/',views.CoursePost.as_view()),
    path('courses/<int:pk>/',views.CourseDetail.as_view()),
    path('courses/<int:pk>/update/',views.CourseUpdate.as_view()),
    path('courses/<int:pk>/delete/',views.CourseDelete.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
