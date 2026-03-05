from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView

from .forms import MissionUpdateForm
from .models import Mission


class MissionListView(ListView):
    model = Mission
    template_name = 'list_missions.html'
    context_object_name = 'missions'


class MissionCreateView(CreateView):
    model = Mission
    template_name = 'update_mission.html'
    form_class = MissionUpdateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        operator_professional_field = context['form'].fields['operator_professional']
        operator_professional_field.queryset = operator_professional_field.queryset.filter(status__status_name='Disponivel')
        operator_fleet_field = context['form'].fields['operator_fleet']
        operator_fleet_field.queryset = operator_fleet_field.queryset.filter(status__status_name='Disponivel')
        return context


class MissionUpdateView(UpdateView):
    model = Mission
    template_name = 'update_mission.html'
    form_class = MissionUpdateForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        operator_professional_field = context['form'].fields['operator_professional']
        operator_professional_field.queryset = operator_professional_field.queryset.filter(Q(status__status_name='Disponivel') | Q(id__in=self.object.operator_professional.all().values_list('id', flat=True)))
        operator_fleet_field = context['form'].fields['operator_fleet']
        operator_fleet_field.queryset = operator_fleet_field.queryset.filter(Q(status__status_name='Disponivel') | Q(id__in=self.object.operator_fleet.all().values_list('id', flat=True)))
        return context
