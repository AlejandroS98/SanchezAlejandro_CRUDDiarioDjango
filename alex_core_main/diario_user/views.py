from django.shortcuts import render
from .models import *
from .forms import UserProfileForm, DiarioMikiForm
from django.urls import reverse_lazy

#GENERICS
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


class CreateProfile(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('profile_createuser')
    template_name = "form_createuser.html"


# ---------- DIARIO ----------

class CreateDiario(CreateView):
    model = DiarioMiki
    form_class = DiarioMikiForm
    success_url = reverse_lazy('diario_list')
    template_name = "form_creatediario.html"


class ListDiario(ListView):
    model = DiarioMiki
    template_name = "list_diario.html"
    context_object_name = "diarios"
    ordering = ['-fecha_creacion']


class DetailDiario(DetailView):
    model = DiarioMiki
    template_name = "detail_diario.html"
    context_object_name = "diario"


class UpdateDiario(UpdateView):
    model = DiarioMiki
    form_class = DiarioMikiForm
    success_url = reverse_lazy('diario_list')
    template_name = "form_creatediario.html"


class DeleteDiario(DeleteView):
    model = DiarioMiki
    success_url = reverse_lazy('diario_list')
    template_name = "confirm_delete_diario.html"
    context_object_name = "diario"