from django.shortcuts import render


# Create your views here.

# "Стартовая" страница
def start_view(request):
    return render(request, "home.html")


# # "Домашняя" страница
# def home_view(request):
#     return render(request, ".html")

# # Страница регистрации
# def signup_view(request):
#     return render(request, "signup.html")
