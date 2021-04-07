from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticateduser


@unauthenticateduser
def loginview(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('training:homepage')

    context = {}
    
    return render(request, 'accounts/login.html', context)


@login_required
def logoutview(request):
    logout(request)
    return redirect('accounts:login')
