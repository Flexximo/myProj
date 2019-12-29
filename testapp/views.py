from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import transaction

from django.views.generic import CreateView, TemplateView
from .forms import ModeratorSignUpForm, AdminSignUpForm
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import My_user
from .models import Invoices

@login_required
def available(request):
    template = loader.get_template('accessed/available.html')
    objects = Invoices.objects.all()
    ct = {'guest': guest, 'objects': objects}
    return HttpResponse(template.render(ct, request))

@login_required
def invoices(request):
    if request.method == "GET":
        template = loader.get_template('accessed/invoices.html')
    return HttpResponse(template.render({}, request))

def index(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render({}, request))

def guest(request):
    template = loader.get_template('accessed/guest.html')
    objects = Invoices.objects.all()
    ct = {'guest': guest, 'objects': objects}
    return HttpResponse(template.render(ct, request))

def registeredUser(request):
    return render(request, 'accessed/invoices.html')

@login_required
def edit(request, param):
    template = loader.get_template("accessed/edit_invoice.html")
    if request.method == "POST":
        if param:
            pk = param
            edit = True
            invoices = Invoices.objects.filter(pk=pk).get()
        else:
            raise Http404
        return HttpResponse(template.render({"pk": pk, "edit": edit, "invoices": invoices}, request))

@login_required
def change_invoice(request, param):
    if request.method == "POST":
        number = request.POST.get("number")
        print(number)
        invoice_date = request.POST.get("invoice_date")
        supply_date = request.POST.get("supply_date")
        comment = request.POST.get("user_comment")

        former = Invoices.objects.filter(pk=param).get()
        former.number = number
        former.date = invoice_date
        former.supply = supply_date
        former.comment = comment
        former.save()

    else:
        raise Http404
    return HttpResponseRedirect(reverse_lazy("available"))

#Удаляем модель с базы
@login_required
def delete_data(request, param):
    if request.method == "POST":
        if param:
            invoices = Invoices.objects.all()
            invoices.filter(pk=param).delete()
        else:
            raise Http404
    return HttpResponseRedirect(reverse_lazy("available"))



# Проверяем данные запроса ajax'a
def check_data(request, param=None):
    import re
    if request.method == "GET":
        if request.GET.get("number"):
            number = request.GET.get("number")
            if re.fullmatch(r"^[INV]{3}-[0-9]{6}$", number):
                for object in Invoices.objects.all():
                    if object.number == number:
                        return HttpResponse("already exists", content_type="text/html")
                return HttpResponse("ok", content_type="text/html")
            else:
                print(False)
                return HttpResponse("no", content_type="text/html")
        if request.GET.get("invoice_date"):
            invoice_date = request.GET["invoice_date"]
            if re.fullmatch(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", invoice_date):
                print("ok")
                return HttpResponse("ok", content_type="text/html")
            else:
                return HttpResponse("no", content_type="text/html")
        if request.GET.get("supply_date"):
            supply_date = request.GET["supply_date"]
            if re.fullmatch(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", supply_date):

                return HttpResponse("ok", content_type="text/html")
            else:
                return HttpResponse("no", content_type="text/html")
        if request.GET.get("comment"):
            user_comment = request.GET["comment"]
            if re.fullmatch(r"[^{}\[\]$()]{2,}", user_comment):
                return HttpResponse("ok", content_type="text/html")
            elif re.fullmatch(r"^$", user_comment):
                return HttpResponse("ok", content_type="text/html")
            else:
                return HttpResponse("no", content_type="text/html")
        return HttpResponse("no", content_type="text/html")
    else:
        return None

#Публикация новой заявки
@login_required
def post_invoice(request):
    if request.method == "POST":
        number = request.POST["number"]
        invoice_date = request.POST["invoice_date"]
        supply_date = request.POST["supply_date"]
        comment = "No comment" if request.POST["user_comment"] == '' else request.POST["user_comment"]
        Invoices.objects.create(date=invoice_date, number=number,
                                supply=supply_date, comment=comment)
        return redirect("available")
    else:
        return HttpResponseRedirect("invoices_page")

#Вьюха для модератора
class ModeratorSignUpView(CreateView):
    model = My_user()
    form_class = ModeratorSignUpForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs = {'user_type': 'moderator', 'level': '0'}
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('available')

#Вьюха для админа
class AdminSignUpView(CreateView):
    model = My_user()
    form_class = AdminSignUpForm
    template_name = "registration/register.html"

    def get_context_data(self, **kwargs):
        kwargs = {'user_type': 'admin', 'level': '1'}
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('available')
