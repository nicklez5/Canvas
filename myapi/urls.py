from django.urls import include, path
from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
from django.conf.urls import url 

app_name = 'myapi'
urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$',RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
    #path('signup', views.UserRegistrationView.as_view()),
    #path('signin', views.UserLoginView.as_view()),
    #path('register', views.register_request,name="register"),
    #path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]