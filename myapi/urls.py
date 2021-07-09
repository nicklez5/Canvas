from django.urls import include, path
from . import views



urlpatterns = [
    path('signup', views.UserRegistrationView.as_view()),
    path('signin', views.UserLoginView.as_view()),
    path('register', views.register_request,name="register"),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]