from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView

from .forms import OperatorProfessionalForm, OperatorFleetForm
from .models import OperatorProfessional, OperatorFleet


class OperatorProfessionalListView(ListView):
    model = OperatorProfessional
    template_name = 'list_professionals.html'
    context_object_name = 'professionals'


class OperatorProfessionalCreateView(CreateView):
    model = OperatorProfessional
    template_name = 'update_professional.html'
    form_class = OperatorProfessionalForm
    success_url = '/profissionais/'


class OperatorProfessionalUpdateView(UpdateView):
    model = OperatorProfessional
    template_name = 'update_professional.html'
    form_class = OperatorProfessionalForm
    success_url = '/profissionais/'


class OperatorFleetCreateView(CreateView):
    model = OperatorFleet
    template_name = 'update_fleet.html'
    form_class = OperatorFleetForm
    success_url = '/frotas/'


class OperatorFleetUpdateView(UpdateView):
    model = OperatorFleet
    template_name = 'update_fleet.html'
    form_class = OperatorFleetForm
    success_url = '/frotas/'


class OperatorFleetListView(ListView):
    model = OperatorFleet
    template_name = 'list_fleets.html'
    context_object_name = 'fleets'
