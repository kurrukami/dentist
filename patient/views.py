from django.shortcuts import render, redirect
from django.views.generic import View, DeleteView, UpdateView
from .forms import *

from ze.shit import *
from ze.decorators import *

from my_users.models import *
decorators =[only_doctors, have_permission]




class patients_gestion_page(View):

    template_name = 'patients_page.html'
    #success_url = template_name
    qs = []
    patients = patient.objects.all()

    @method_decorator(decorators)
    def get(self, request):


        self.patients = patient.objects.all().filter(adminn=request.user)
        from_me_to_me(patients=self.patients)
        from_me_to_me(p=patient.objects.all().filter(adminn=request.user))
        context = {
                 'patients' : self.patients
                }
        from_me_to_me(get=request.GET)
        search_query = request.GET.get('search_by_name')
        from_me_to_me(search_query=search_query)
        if search_query:
            self.qs = self.search_by_name(search_query)
            from_me_to_me(qs=self.qs)
            context = {
                     'patients' : self.qs
                    }
            if len(self.qs) == 0:
                msg = f'sorry, u dont have any patients with the name {search_query}'
                from_me_to_me(msg=msg)
                messages.error(request, msg)
            else:
                results = [x for x in self.qs if x.is_deleted is not True]
                from_me_to_me(r=results)
                msg = f'{len(results)} results was found ---> {search_query}'
                from_me_to_me(msg=msg)
                messages.success(request, msg)

        return render(request, self.template_name, context)

    def search_by_name(self, search_query):
        self.qs = self.patients.filter(name__icontains=search_query)
        return self.qs

    def search_by_year(self, search_query):
        self.qs = self.patients.filter(date_debut__icontains=search_query)
        return self.qs

    @method_decorator(only_doctors)
    @method_decorator(have_permission)
    def delete_patient_fake(request, pk):
        try:
            p = patient.objects.get(pk=pk)
            from_me_to_me(p=p.is_deleted)
            if not p.is_deleted:
                p.deleted()
                p.save()
                msg = f'{patient.name} was deleted successfully'
                from_me_to_me(msg=msg)
                messages.error(request, msg)

        except patient.DoesNotExist :
            msg = 'patient not found'
            from_me_to_me(msg=msg)
            messages.error(request, msg)

        return redirect("all_patients")


@only_doctors
@have_permission
def update_patient2(request, pk):
    form = patient_form
    try:
       p = patient.objects.get(pk=pk)
       from_me_to_me(msg=request.POST)
       f = form(request.POST or None, instance=p)
       if f.is_valid():
           f.save()
           msg = f'{p.name} was updated successfully'
           from_me_to_me(msg=msg)
           messages.error(request, msg)
           return redirect("all_patients")

    except patient.DoesNotExist:
        msg = 'DoesNotExist'
        return redirect("all_patients")

    context = {
            'form':f,
    }
    return render(request, 'patient_form_view.html', context)

@only_doctors
@have_permission
def delete_patient_real(request, pk):
    try:
        p = patient.objects.get(pk=pk)
        from_me_to_me(p=p.is_deleted)
        p.delete()
        msg = f'{patient.name} was deleted successfully'
        from_me_to_me(msg=msg)
        messages.error(request, msg)

    except patient.DoesNotExist :
        msg = 'patient does not found'
        from_me_to_me(msg=msg)

    return redirect("all_patients")



class add_new_patient(View):

    template_name = 'patient_form_view.html'
    form = patient_form



    @method_decorator(decorators)
    def get(self, request):

        context = {
                 'form' : self.form,
        }
        return render(request, self.template_name, context)

    @method_decorator(decorators)
    def post(self, request):

        u_id = request.user.id
        user = doctor.objects.get(pk=u_id)
        from_me_to_me(u_id=u_id)
        #from_me_to_me(dt=request.POST)
        f = self.form(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            #cd.setdefault('adminn', u_id)
            from_me_to_me(cd=cd)
            try:
                pastient = patient.objects.get(cin=cd["cin"])
                msg = 'tht patient is alrady there'
                from_me_to_me(msg=msg)
                messages.error(request, msg)
                return redirect("add_new_patient")
            except patient.DoesNotExist:
                pastient = patient.objects.create(
                adminn = user,
                name = cd["name"],
                phone_num = cd["phone_num"],
                cin = cd["cin"],
                genre_visite = cd["genre_visite"],
                montant_a_payer = cd["montant_a_payer"],
                montant_paye = cd["montant_paye"],
                commentaire = cd["commentaire"]
                )
                msg = f'patient {patient.name} was created'
                from_me_to_me(msg=msg)
                messages.error(request, msg)
                return redirect("all_patients")
        else:
            self.form = self.form(request.POST)
            from_me_to_me(err=f.errors)
            msg = 'form not valid'
            from_me_to_me(msg=msg)
            messages.error(request, f.errors)
            return self.get(request)
