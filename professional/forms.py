from django import forms
from .models import OperatorProfessional, OperatorFleet


class OperatorProfessionalForm(forms.ModelForm):
    class Meta:
        model = OperatorProfessional
        fields = ['name', 'role', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class OperatorFleetForm(forms.ModelForm):
    class Meta:
        model = OperatorFleet
        fields = ['fleet_type', 'fleet_model', 'status']
        widgets = {
            'fleet_type': forms.TextInput(attrs={'class': 'form-control'}),
            'fleet_model': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

