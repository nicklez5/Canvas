from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('assignments/',views.AssignmentList()),
    path('assignments/post',views.AssignmentPost()),
    path('assignments/<int:pk>/',views.AssignmentDetail.as_view()),
    path('assignments/<int:pk>/update/',views.AssignmentUpdate.as_view()),
    path(''
]