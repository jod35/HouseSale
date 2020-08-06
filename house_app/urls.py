from django.urls import path
from . import views

app_name='appl'

urlpatterns = [
    path('',views.index,name='home')
]