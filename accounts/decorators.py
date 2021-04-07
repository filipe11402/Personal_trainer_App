from django.shortcuts import redirect


def unauthenticateduser(viewfunc):
    def inner_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('training:homepage')      
        else:
            return viewfunc(request, *args, **kwargs)

    return inner_func
