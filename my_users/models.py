from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
"""def create_user(self, username, email, phone_num):
    if not username:
        raise ValidationError("u have a name don't u")
    if not email:
        raise ValidationError("ur email plz ")
    if not phone_num:
        raise ValidationError("u must have phone_num so i can call u negga!!")

    user = self.model(
    username = username,
    email = self.normalize_email(email),
    phone_num = phone_num
    )
    user.set_password(password)
    user.save(using=self._db)
    return user"""

"""class adminnManager(UserManager):


    def create_superuser(self, username, email, password=None):
        if not email:
            raise ValidationError("enter ur email u negga!!")

        user = self.model(
        username = username,
        email = self.normalize_email(email),
        password = password
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.type = User.types.ADMIN
        user.save(using=self._db)
        return user
"""




class User(AbstractUser):

    class types(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        DOCTOR = "DOCTOR", "doctor"

    type = models.CharField(
    choices=types.choices,
    default=types.DOCTOR,
    max_length=50)


    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    phone_num =  models.CharField(max_length=11)

    description = models.TextField(blank=True)


    first_name = None
    last_name = None


    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    #objects = adminnManager()


    def get_url(self):
        return f'home/users/{self.pk}/MaybeDumpOne/{self.username}'

    def get_created_time(self):
        msg = '{:%A %B, %d,  time %H:%M:%S.}'
        return msg.format(self.created)

    def get_last_login(self):
        msg = '{:%A %B, %d,  time %H:%M:%S.}'
        return msg.format(self.last_login)


    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ('-created',)
        unique_together = ('email',)



class adminnManager(UserManager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.types.ADMIN)

class doctorManager(UserManager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.types.DOCTOR)



class adminn(User):

    objects = adminnManager()


    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.types.ADMIN
            #self.is_superuser = True
        return super().save(*args, **kwargs)


class doctor(User):

    objects = doctorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.types.DOCTOR
        return super().save(*args, **kwargs)




class adminn_infos(models.Model):

    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    phone_num =  models.CharField(max_length=11)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id:{self.pk}_owner:{self.username}'
