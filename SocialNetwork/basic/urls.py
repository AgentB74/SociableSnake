from django.urls import path
from basic import views
from users.views import SignUp

urlpatterns = [
    # path('home/', views.home_view),
    path('', views.start_view),
    # path('about', views.about),
    # path('contact', views.contact),
]