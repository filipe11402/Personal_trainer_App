from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticateduser
from .forms import CustomUserCreationForm


@unauthenticateduser
def loginview(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('training:homepage-pt')

    context = {}
    
    return render(request, 'accounts/login.html', context)


@login_required
def logoutview(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def registerview(request):

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
        return redirect('training:admin-panel')

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)
