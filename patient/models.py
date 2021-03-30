from django.db import models
from ze import settings

# Create your models here.
import datetime


class patient(models.Model):

    adminn = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=11)
    cin = models.CharField(unique=True, max_length=11)

    genre_visite = models.CharField(max_length=500)
    montant_a_payer = models.PositiveIntegerField()
    montant_paye = models.PositiveIntegerField(default=0)

    date_debut = models.DateTimeField(auto_now_add=True)

    commentaire = models.CharField(max_length=500, blank=True)

    is_deleted = models.BooleanField(default=False)

    is_completed = models.CharField(max_length=50, default='Not completed')


    def make_date_fin(self):
        date_fin = datetime.datetime.now()
        msg = '{:%A %B,  time %H:%M:%S.}'
        return msg.format(date_fin)

    def deleted(self):
        self.is_deleted = True
        self.is_completed = self.make_date_fin()
        return 'ok'


    def __str__(self):
        return f'patient Mr/Miss: {self.name} \n Respo Mr/Miss: {self.adminn}'

    def dh_format(self, montant):
        montant = str(montant)
        return f'{montant} dh'



    def cost_dh(self):
        return self.dh_format(self.montant_a_payer)

    def payed_dh(self):
        return self.dh_format(self.montant_paye)

    def rest_dh(self):
        return self.dh_format(self.montant_reste())



    def montant_reste(self):
        montant = self.montant_a_payer
        paye = self.montant_paye
        return (montant - paye)


    def get_date_debut(self):
        msg = '{:%A %B,  time %H:%M:%S.}'
        return msg.format(self.date_debut)




    class Meta:
          ordering = ('-date_debut',)
           #unique_together = ('email',)
