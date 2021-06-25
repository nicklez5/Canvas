from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students',views.StudentViewSet)
router.register(r'lectures',views.LectureViewSet)
router.register(r'courses',views.CourseViewSet)
router.register(r'assignments',views.AssignmentViewSet)

urlpatterns = [
    path('signup', views.UserRegistrationView.as_view()),
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]