from django.urls import path
from django.views.generic.base import TemplateView
from .views import *
urlpatterns = [
    path('',TemplateView.as_view(template_name= 'accounts/index.html'),name='Home1'),
    path('signup',SignUpView.as_view(),name = 'SignUp'),
    path('signin',SignInView.as_view(),name = 'SignIn'),
    path('signout',SignOutView.as_view(),name = 'SignOut'),
    path('adminsignup',AdminSignUpView.as_view(),name='AdminSignUp'),
    
]