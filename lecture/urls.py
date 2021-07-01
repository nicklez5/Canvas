from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 
urlpatterns = [
    path('lectures/',views.LectureList.as_view()),
    path('lectures/post/',views.LecturePost.as_view()),
    path('lectures/<int:pk>/', views.LectureDetail.as_view()),
    path('lectures/<int:pk>/update/',views.LectureUpdate.as_view()),
    path('lectures/<int:pk>/delete/',views.LectureDelete.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
