from django.urls import path
from . import views

app_name='appl'

urlpatterns = [
    path('',views.index,name='home'),
    path('signup/',views.create_account,name='register'),
    path('login/',views.login,name='login'),
]