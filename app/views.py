from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here

from app.forms import *


def home_page(request):
        
    return render(request,'home_page.html')

def Registration(request):
    UO=UserForm()
    PO=ProfileForm()
    d={'UO':UO,'PO':PO}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
           NSUO=ufd.save(commit=False)
           NSUO.set_password(ufd.cleaned_data['password'])
           NSUO.save()
           NSPO=pfd.save(commit=False)
           NSPO.username=NSUO
           NSPO.save()
           
           send_mail('Registration',
                     'Registration is successfully done',
                     'chandanakamalapuram@gmail.com',
                     [NSUO.email],
                     fail_silently=False,


           )

           return HttpResponse('Registration is successfully done....!')
        else:
            return HttpResponse('Data Is Invalid')









    return render(request,'Registration.html',d)
