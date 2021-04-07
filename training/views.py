from django.shortcuts import render


def indexview(request):

    current_user = request.user

    context = {
        'user': current_user,
    }

    return render(request, 'training/index_client.html', context)

