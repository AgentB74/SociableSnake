from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^list/', views.UserView.as_view(), name="user_list"),
]
