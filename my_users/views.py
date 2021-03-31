from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from ze import settings

from ze.shit import *
from ze.decorators import *

from django.core.exceptions import ObjectDoesNotExist

from ze.decorators import *

#from my_users.authentication import email_auth

# Create your views here.

decorators =[only_superusers]

@only_superusers
def delete_doctor_real(request, pk):
    try:
        d = doctor.objects.get(pk=pk)
        from_me_to_me(doctor=request.user)
        if d.is_superuser:
            msg = f'{d.username} is superuser, u r a traitor'
            from_me_to_me(msg=msg)
            messages.error(request, msg)
            return redirect("admin_view", "doctors")

        d.delete()
        msg = f'{d.username} was deleted successfully'
        from_me_to_me(msg=msg)
        messages.error(request, msg)

    except doctor.DoesNotExist :
        msg = 'doctor does not found'
        from_me_to_me(msg=msg)

    return redirect("admin_view", "doctors")


class view(View):
    template_name = 'base.html'
    def get(self, request):
        return render(request, self.template_name, {})


from django.contrib.auth import logout
def log_out(request):
    logout(request)
    return redirect('login')


@only_superusers
def get_adminn_pk(request, pk):
    op = send_email(pk)
    if op.check_doctor():
        try:
            msg = 'send email process .........'
            from_me_to_me(msg=msg)
            pswd = op.generate_pswd()
            from_me_to_me(pswd='password generated ...')
            msg = op.generate_msg()
            from_me_to_me(msg='msg generated ...')
            if op.send_him_mail() is not None:
                msg = 'send_email_process complited'
                doc = op.create_doctor()
                from_me_to_me(doctor='doctor created ...')
                from_me_to_me(msg=msg)
                messages.success(request, msg)
            else:
                msg = 'try again'
                from_me_to_me(msg=msg)
                messages.success(request, msg)


        except:
            msg = 'send email process failed'
            from_me_to_me(msg=msg)
            messages.success(request, msg)

    else:
        msg = 'this doctor is alrady here'
        from_me_to_me(msg=msg)
        messages.success(request, msg)

    del op
    try:
        from_me_to_me(op=op)
    except :
         from_me_to_me(op='op deleted')
    return redirect('admin_view', 'doctors_infos')


from django.core.mail import send_mail
import random, math
class send_email:

    def __init__(self, pk):

        try:
            self.info = adminn_infos.objects.get(pk=pk)
        except adminn_infos.DoesNotExist:
            msg = 'pk not found'
            messages.success(request, msg)
            return redirect("view")

        self.username = self.info.username
        self.to_email = self.info.email
        self.phone_num = self.info.phone_num
        self.msg = ''
        self.password = ''

    def check_doctor(self):
        try:
            doc = doctor.objects.get(email=self.to_email)
            return False
        except doctor.DoesNotExist:
            return True


    from_email = settings.EMAIL_HOST_USER
    subject = 'your password'


    def generate_msg(self):
        msg1 = f'we are glad u join our large community  {self.username}.\n'
        msg2 = f'here is ur password : {self.password}.\n\n '
        msg3 =  'here is our website https://shikay.herokuapp.com/ and thank u for choosing us'
        self.msg = msg1+msg2+msg3
        from_me_to_me(msg=self.msg)
        return self.msg

    def generate_pswd(self):
        rn = random.random()*1000000
        rn = math.floor(rn)
        rn = str(rn)
        pwd = self.username+rn
        self.password = pwd
        from_me_to_me(pswd=self.password)
        return self.password

    def create_doctor(self):
        user = doctor.objects.create(username=self.username,
                                         email=self.to_email,
                                         phone_num=self.phone_num)
        user.set_password(self.password)
        user.save()
        msg = 'doctor has been created'
        from_me_to_me(msg=msg)
        return user


    def send_him_mail(self):
        try:
            send_mail(self.subject,
            self.msg,
            self.from_email,
            [self.to_email],
            fail_silently=False)
            msg = 'email has sent'
            from_me_to_me(msg=msg)
            from_me_to_me(msg=self.to_email)
            return 11
        except:
            msg = 'email is None'
            from_me_to_me(msg=msg)
            return None

@only_superusers
def superuser_page(request):
    template_name = 'superuser_page.html'
    return render(request, template_name, {})


class admin_view(View):

    @method_decorator(decorators)
    def get(self, request, key):
        #from_me_to_me(doctor=request.user.is_superuser)
        doctors = doctor.objects.all()
        doctors_infos = adminn_infos.objects.all()
        smtg = {
        "doctors": ("doctors.html", doctors),
        "doctors_infos": ("doctors_infos.html", doctors_infos)
        }
        if key in smtg.keys():
            if len(doctors) == 0:
                msg = 'no one want to join us yet :))'
                messages.success(request, msg)
            if len(doctors_infos) == 0:
                msg = 'u dt have any doctors yet :))'
                messages.success(request, msg)
            return render(request, smtg[key][0], {'smtg': smtg[key][1]})


class login_view(View):

    template_name = 'login.html'
    form = login_form

    def get(self, request):
        #from_me_to_me(request=dir(request))
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        f = self.form(request.POST)

        if f.is_valid():
            cd = f.cleaned_data
            #from_me_to_me(cd=cd)
            username = cd["username"]
            password = cd["password"]
            user = authenticate(request, username=username, password=password)
            from_me_to_me(user=user, ur=request.user)
            if user is not None and user.is_active:
                login(request, user)
                from_me_to_me(user=user, ur=request.user)
                if user.is_superuser:
                    #admin = admin_view()
                    msg = f'supperuser {user.username}, glad to see u again'
                    from_me_to_me(msg=msg)
                    messages.success(request, msg)
                    return redirect("admin_view", 'doctors_infos')

                msg = f'welcom {user.username}, glad to see u again'
                from_me_to_me(msg=msg)
                messages.success(request, msg)
                return redirect("view")
            else:
                msg = 'user not found, im calling FBA'
                from_me_to_me(msg=msg)
                messages.success(request, msg)
                return redirect("login")
        else:
            msg = 'smtg went wrong plz try again'
            from_me_to_me(msg=msg)
            messages.success(request, msg)
            return redirect("login")


class send_infos_view1(View):
    template_name = 'send_infos1.html'
    def get(self, request):
        return render(request, self.template_name, {})


def send_infos_view(request):
    from_me_to_me(method=request.method)
    form = adminn_infos_form
    #from_me_to_me(form=form)
    if request.method == 'POST':
        f = form(request.POST)
        #from_me_to_me(data=f)
        if f.is_valid():
            cd = f.cleaned_data
            from_me_to_me(cleaned_data=cd)
            infos = adminn_infos.objects.create(
            username = cd["username"],
            email = cd["email"],
            phone_num = cd["phone_num"]
            )
            from_me_to_me(infos=infos)
            msg = 'ur request has been sent, merci'
            messages.success(request, msg)
            return redirect("send_infos")
        else:
            from_me_to_me(err=f.errors)
            msg = f.errors
            messages.error(request, msg)
            return redirect("send_infos")
    return render(request, "send_infos.html", {'form' : form })
