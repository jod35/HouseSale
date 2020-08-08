from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import House, WareHouse,Land

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


#view for creating a house
class HouseCreationView(CreateView):
    model=House
    fields=['name','price','location','bedrooms','bathrooms','toilets','image1']
    template_name='house_app/addhouse.html'
    success_url=''
