from django.contrib.auth import  login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def coustmer_page(request):
    return render(request,'home.html')
@login_required
def courier_page(request):
    return render(request,'home.html')
def sign_up(request):
    form = forms.SignUPForm()
    if request.method =='POST':
        form = forms.SignUPForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email').lower()
            user=form.save(commit=False)
            user.username=email
            user.save()

            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')

    return render(request,'sign_up.html',{
        'form': form
    })
    