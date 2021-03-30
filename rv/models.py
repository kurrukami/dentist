from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from my_users.models import adminn
from my_users.models import doctor

# Create your models here.




class rv(models.Model):



    doc_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=11)
    cmnt = models.CharField(max_length=111)

    rd_time = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'respo: {self.doc_name}\nMr/Miss: {self.name}'

    def date_forma(self):
        msg = '{:%B %d %Y, %H:%M}'
        return msg.format(self.rd_time)

    class Meta:
        ordering = ('created', '-rd_time',)
