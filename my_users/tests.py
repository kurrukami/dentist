from django.test import TestCase, Client
from django.urls import reverse
from my_users.models import *
#from my_users.views import
from ze.shit import *

from my_users.views import doctor_register
# Create your tests here.

class Test_register(TestCase):

    def test_change(self):
        try:
            doc = doctor.objects.get(id = 2)
            doc.autorized = True
            return 'good'
        except doctor.DoesNotExist:
            msg = 'doctor not found'
            return msg
