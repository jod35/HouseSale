from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import House, WareHouse,Land
from .forms import LandCreationForm,WareHouseCreationForm,HouseCreationForm

# Create your views here.

def index(request):
    return render(request,'house_app/index.html')


def create_account(request):
    form=RegistrationForm()

    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully, You can login.')

            return redirect('/login')

        
    context={
        'form':form
    }
    return render(request,'house_app/signup.html',context)

#dashboard_view
def user_dashboard(request):
    houses=House.objects.order_by('-id').all()
    warehouses=WareHouse.objects.order_by('-id').all()
    land=Land.objects.order_by('-id').all
    context={
        'houses':houses,
        'warehouses':warehouses,
        'land':land
    }
    return render(request,'house_app/dashboard.html',context)

#view for creating a house

def create_house(request):
    form=HouseCreationForm()
    if request.method == 'POST':
        form=HouseCreationForm(request.POST,request.FILES)

        if form.is_valid():
            obj=form.save(commit=False)

            obj.dealer=request.user

            obj.save()

            messages.success(request,"House has been created successfully")

            return redirect('/dashboard/')
            
    context={
        'form':form
    }
    return render(request,'house_app/addhouse.html',context)


#view for creating a warehouse
def create_warehouse(request):
    form=WareHouseCreationForm()
    context={
        'form':form
    }
    return render(request,'house_app/addwarehouse.html',context)


#view for creating a land deal
def create_land(request):
    form=LandCreationForm()
    context={
        'form':form
    }

    return render(request,'house_app/addland.html',context)
    

