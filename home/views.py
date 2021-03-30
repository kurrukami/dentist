from django.shortcuts import render, redirect
from django.views.generic import View
#from .forms import *
#from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

from ze.shit import *


from django.core.exceptions import ObjectDoesNotExist

from ze.decorators import *

# Create your views here.

def home(request):
    return render(request, "home.html", {})


class home_pages(View):

    context = {}
    templates = {
    "home" : "home.html",
    'about': 'about.html',
    'contact': 'contact.html',

    }

    def check_key(self, key):
        from_me_to_me(key=self.templates.keys())
        if isinstance(key, str):
            if key in self.templates.keys():
                template_name = self.templates[key]
                return template_name
        else:
            return None
        pass
    def get(self, request, key):
        template_name = self.check_key(key)
        if template_name is not None:
            return render(request, template_name, context)
        return render(request, '404_page.html', context)
