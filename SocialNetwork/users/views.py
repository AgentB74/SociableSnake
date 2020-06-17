from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

# Страница регистрации
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    # В случае успеха перенаправление на страницу авторизации
    success_url = reverse_lazy('login')
    # Сама страница регистрации
    template_name = 'signup.html'


# Список пользователей
class UserView(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')
    model = CustomUser
    # template_name = 'users/list.html'
    # success_url = reverse_lazy('edit_page')
    # success_msg = 'nect'
    # fields = ['first_name', 'last_name']

    # def get_queryset(self):
    #     print("sas")
    #     users = self.model.objects.all(self)
    #     print(users)
    #     return render(self.request, 'users/list.html', {'users': users})
    def get(self, request):
        try:
            users = self.model.objects.all()
        except self.model.DoesNotExist:
            return HttpResponse(status=404)
        return render(request, 'users/list.html', {'users': users})
