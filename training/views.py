from django.shortcuts import render
from .decorators import *
from accounts.models import PersonalTrainer, Client, CustomUser
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
@onlypt
def personalview(request):

    # fetch current personal trainer
    user = CustomUser.objects.get(id=request.user.id)
    personal = PersonalTrainer.objects.get(username=user)

    # fetch total of clients
    total_clients = personal.client_set.all()
    number_clients = total_clients.count()



    context = {
        'number_clients': number_clients,
        'total_clients': total_clients,
    }

    return render(request, 'training/index_pt.html', context)

@login_required(login_url='accounts:login')
def indexview(request):

    # fetch all training plans 
    training_plans = request.user.client.planotreino_set.all()
    

    context = {
        'training_plans': training_plans,
    }

    return render(request, 'training/index_client.html', context)


@login_required
@adminonly
def adminview(request):

    # fetch all users but not the admin
    all_pts = PersonalTrainer.objects.all()
    all_clients = Client.objects.all()

    context = {
        'all_pts': all_pts,
        'all_clients': all_clients,
    }

    return render(request, 'training/dashboard.html', context)
