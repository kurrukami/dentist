from django.shortcuts import redirect, render
from django.contrib import messages
from ze.shit import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

context = {}
def only_doctors(view_func):
    def wrapper_func(request, *args,**kwargs):
        u = request.user
        if u.is_authenticated:
            if u.type == "DOCTOR" or u.is_superuser:
                from_me_to_me(msg="decorator works")
                return view_func(request, *args,**kwargs)
            else:
                from_me_to_me(msg="decorator works")
                template_name = 'not_allowed_page.html'
                return  render(request, template_name, context)
            return
        else:
            msg = 'you r not loged in , plz log in'
            from_me_to_me(msg=msg)
            messages.error(request, msg)
            return redirect("login")
    return wrapper_func


def only_superusers(view_func):
    def wrapper_func(request, *args, **kwargs):
        u = request.user
        if u.is_authenticated:
            if u.is_superuser:
                from_me_to_me(msg='seems u r admin '+u.username)
                return view_func(request, *args, **kwargs)
            else:
                from_me_to_me(msg='u r not an admin')
                template_name = 'not_allowed_page.html'
                return  render(request, template_name, context)
        else:
            msg = 'you r not loged in , plz log in'
            from_me_to_me(msg=msg)
            messages.error(request, msg)
            return redirect("login")

    return wrapper_func


def have_permission(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.autorized == False:
            from_me_to_me(msg='you dont have permissions yet :))')
            from_me_to_me(msg="decorator works")
            template_name = 'dont_have_permissions.html'
            msg='this page requires some permissions that you dont have yet :))'
            context.setdefault('user', request.user)
            context.setdefault('msg', msg)
            return  render(request, template_name, context)
        else:
            msg='seems tht u have payed urs taxes:))'
            from_me_to_me(msg='msg')
            return  view_func(request, *args,**kwargs)

    return wrapper_func
