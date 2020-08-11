from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'appl'

urlpatterns = [
    path('' , views.index , name = 'home') , 
    path('signup/' , views.create_account , name = 'register') , 
    path('login/' , auth_views.LoginView.as_view(template_name = 'house_app/login.html') , name = 'login') , 
    path('logout/' , auth_views.LogoutView.as_view(template_name = 'house_app/loggedout.html') , name = 'logout') , 
    path('addhouse/' , views.create_house , name = 'create_house') , 
    path('view_houses/' , views.house_admin , name = 'view_houses') , 
    path('addwarehouse/' , views.create_warehouse , name = 'create_warehouse') , 
    path('addland/' , views.create_land , name = 'create_land') , 
    path('update_house/<pk>/' , views.HouseUpdateView.as_view() , name = 'update_house') , 
    path('delete_house/<id>/' , views.delete_house , name = 'delete_house') , 
    path('view_warehouses/' , views.view_warehouses , name = 'view_warehouses') , 
    path('update_warehouse/<pk>' , views.WareHouseUpdateView.as_view() , name = 'update_warehouse') , 
    path('dashboard/' , views.user_dashboard , name = 'user_dashboard') , 

]