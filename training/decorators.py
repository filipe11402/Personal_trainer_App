from django.shortcuts import redirect


def onlypt(viewfunc):
    def inner_func(request, *args, **kwargs):
        if request.user.is_client:
            return redirect('training:homepage-client')
        elif request.user.is_pt:
            return viewfunc(request, *args, **kwargs)
    return inner_func
