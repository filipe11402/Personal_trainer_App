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
        print(request.POST)

        if form.is_valid():
            user = form.save()

            user.refresh_from_db()

            # check whether value passed from form is_pt or is_client
            if form.cleaned_data.get('role') == 'is_pt':
                user.is_pt = True
                user.is_client = False
            else:
                user.is_pt = False
                user.is_client = True
            
            user.save()
            return redirect('training:admin-panel')

    context = {}

    return render(request, 'accounts/register.html', context)
