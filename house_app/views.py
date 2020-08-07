from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic import CreateView

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


