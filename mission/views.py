from django.shortcuts import render
from django.views.generic import ListView

from .models import Mission


class MissionListView(ListView):
    model = Mission
    template_name = 'list_missions.html'
    context_object_name = 'missions'
