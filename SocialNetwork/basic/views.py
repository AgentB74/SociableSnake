from django.shortcuts import render


# Create your views here.

# "Стартовая" страница
def start_view(request):
    return render(request, "start.html")


# "Домашняя" страница
def home_view(request):
    return render(request, "reg.html")

# # Страница регистрации
# def signup_view(request):
#     return render(request, "signup.html")
