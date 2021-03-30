from .models import *
from django.core.exceptions import ObjectDoesNotExist




"""class email_auth(object):

    def authenticate(self, request, username=None, password=None, **args):
        #email = args["email"]
        #password = args["password"]
        try:
            u = adminn.objects.get(email=username)
            if u.check_password(password):
                return u
            return None
        except u.ObjectDoesNotExist:
            return None


    def get_user(self, user_id):
        try:
            user = adminn.objects.get(pk=user_id)
            return user
        except user.DoesNotExist:
            return None

    def get_user_by_email(self, email):
        try:
            return adminn.objects.get(email=email)
        except adminn.DoesNotExist:
            return None

    def __str__(self):
        return 'email_auth:class'
"""
