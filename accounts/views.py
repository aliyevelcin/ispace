from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth.views import LoginView
from accounts.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy

class Register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:login')

class Login(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('core:profile')


def profile(request):
    return render(request, 'profile.html')
