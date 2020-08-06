from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='appl'

urlpatterns = [
    path('',views.index,name='home'),
    path('signup/',views.create_account,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='house_app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='house_app/loggedout.html'),name='logout'),
]