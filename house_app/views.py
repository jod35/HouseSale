from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request,'house_app/index.html')


def create_account(request):
    form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'house_app/signup.html',context)


def login(request):
    return render(request,'house_app/login.html')