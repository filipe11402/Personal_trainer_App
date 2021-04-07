from django.shortcuts import render
from .decorators import *


@onlypt
def personalview(request):

    context = {}

    return render(request, 'training/index_pt.html', context)


def indexview(request):

    context = {}

    return render(request, 'training/index_client.html', context)



