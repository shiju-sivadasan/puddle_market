from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
urlpatterns = [
    path('',views.base,name='index'),
    path('index/',views.index,name='base'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form = LoginForm),name='login'),
]