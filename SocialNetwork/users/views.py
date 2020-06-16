from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

# Страница регистрации
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    # В случае успеха перенаправление на страницу авторизации
    success_url = reverse_lazy('login')
    # Сама страница регистрации
    template_name = 'signup.html'
