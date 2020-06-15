from django.urls import path
from basic import views

urlpatterns = [
    path('', views.signup_view),
    path('/home', views.home_view),
    # path('about', views.about),
    # path('contact', views.contact),
]