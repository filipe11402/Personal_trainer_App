from django.shortcuts import redirect


def onlypt(viewfunc):
    def inner_func(request, *args, **kwargs):
        if request.user.is_pt:
            return viewfunc(request, *args, **kwargs)
        elif request.user.is_client:
            return redirect('training:homepage-client')
    return inner_func


def adminonly(viewfunc):
    def inner_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return viewfunc(request, *args, **kwargs)
        else:
            return redirect('training:homepage-pt')
    return inner_func
