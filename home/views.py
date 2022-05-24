from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

class Welcome(TemplateView):
   template_name = 'home/welcome.html'

class LoginInterfaceView(LoginView):
   template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
   template_name = 'home/logout.html'

class SignupView(CreateView):
   form_class = UserCreationForm
   template_name = 'home/register.html'
   success_url = '/notes'
