from django import forms
from .models import Mission

from professional.models import OperatorProfessional, OperatorFleet


class MissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['mission_date', 'description', 'operator_professional', 'operator_fleet', 'status']
        widgets = {
            'mission_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    operator_professional = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        queryset=OperatorProfessional.objects.all()
    )

    operator_fleet = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        queryset=OperatorFleet.objects.all()
    )
