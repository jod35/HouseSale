from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import House, WareHouse,Land
from .forms import LandCreationForm,WareHouseCreationForm,HouseCreationForm

# Create your views here.

def index(request):
    return render(request,'house_app/index.html',context={'title':"Welcome to HouseSale"})


def create_account(request):
    form=RegistrationForm()

    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():

            form.save()

            messages.success(request,'Account Created Successfully, You can login.')

            return redirect('/login')

        
    context={
        'form':form,
        'title':'Create Your Account'
    }
    return render(request,'house_app/signup.html',context)

#dashboard_view
def user_dashboard(request):
    houses = House.objects.order_by('-id').all()

    warehouses = WareHouse.objects.order_by('-id').all()

    land = Land.objects.order_by('-id').all

    context = {
        'houses' : houses,
        'warehouses' : warehouses,
        'land' : land,
        'title' : 'User Dashboard'
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
        'form':form,
        'title':"Create A House"
    }
    return render(request,'house_app/addhouse.html',context)

#view for showing houses
def house_admin(request):
    houses = House.objects.filter(dealer=request.user).all()

    context = {
        'title' : "House Admin",
        'houses' : houses
    }
    return render(request,'house_app/houses.html',context)

class HouseUpdateView(UpdateView):
    model = House

    fields=  ['name','location','price','bathrooms','bedrooms','toilets','sitting_room','swimming_pool','image1']
    
    template_name = 'house_app/updatehouse.html'
    
    success_url = '/view_houses'
    
    context_object_name = 'house'

def delete_house(request,id):

    house = House.objects.get(id=id)

    if request.method == 'POST':

        house.delete()
        
        messages.success(request,"House Deleted Successfully")
        
        return redirect('/view_houses/')
    
    context = {
        'house':house
    }
    
    return render(request,'house_app/deletehouse.html',context)

#view for creating a warehouse
def create_warehouse(request):

    form=WareHouseCreationForm()

    if request.method == 'POST':

        form = WareHouseCreationForm(request.POST)

        if form.is_valid():

            obj = form.save(commit=False)

            obj.dealer = request.user

            obj.save()

            return redirect('/view_warehouses/')


    context={
        'form':form
    }
    return render(request,'house_app/addwarehouse.html',context)

#list view for warehouses
def view_warehouses(request):
    warehouses = WareHouse.objects.filter(dealer=request.user).all()

    context={
        "title" : "Warehouse Admin",
        "warehouses" : warehouses
    }

    return render(request,'house_app/warehouses.html',context)

#update a warehouse 

class WareHouseUpdateView(UpdateView):
    model = WareHouse

    fields = ['name','location','price','space','image1']

    success_url = '/view_warehouses/'

    template_name = 'house_app/updatewarehouse.html'


#view for creating a land deal
def create_land(request):
    form = LandCreationForm()

    context = {
        'form':form
    }

    return render(request,'house_app/addland.html',context)
    



    