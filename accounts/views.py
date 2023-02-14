from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from .models import MyUser
from .forms import *

# Create your views here.
class SignUpView(SuccessMessageMixin,CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('SignIn')
    success_message = 'signed up successfully'

class SignInView(SuccessMessageMixin,LoginView):
    template_name = 'accounts/signin.html'
    success_message = 'Logged in successfully'

class SignOutView(SuccessMessageMixin,LogoutView):
    template_name = 'foodapp/index.html'
    success_message = 'Loged out'

class AdminSignUpView(SuccessMessageMixin,CreateView):
    model = MyUser
    form_class = MyAdminCreationForm
    template_name = 'accounts/adminsignup.html'
    success_url = reverse_lazy('Home1')