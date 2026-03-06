from django import forms
from .models import Mission

class MissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['mission_date', 'description', 'operator_professional', 'operator_fleet', 'status']
        
        # Definindo as labels aqui para que o {{ form.as_p }} ou {{ form.as_table }} 
        # as renderize automaticamente com a estética Sci-Fi
        labels = {
            'mission_date': 'DATA_DA_MISSÃO',
            'description': 'DESCRIÇÃO_TÁTICA',
            'operator_professional': 'PROFISSIONAIS_OPERADORES',
            'operator_fleet': 'FROTAS_OPERACIONAIS',
            'status': 'STATUS_ATUAL',
        }

        widgets = {
            # Classes adaptadas para inputs
            'mission_date': forms.DateInput(attrs={
                'class': 'w-full p-2 bg-[#05080a]/60 border border-[#6ac2b9]/30 text-[#e2e8f0] focus:border-[#6ac2b9] focus:outline-none transition-colors', 
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 bg-[#05080a]/60 border border-[#6ac2b9]/30 text-[#e2e8f0] resize-none focus:border-[#6ac2b9] focus:outline-none transition-colors',
                'rows': 3
            }),
            'status': forms.Select(attrs={
                'class': 'w-full p-2 bg-[#05080a]/60 border border-[#6ac2b9]/30 text-[#e2e8f0] cursor-pointer focus:border-[#6ac2b9] focus:outline-none transition-colors'
            }),
            
            # Transferidos para o Meta para manter a estrutura padrão do Django
            'operator_professional': forms.CheckboxSelectMultiple(attrs={
                'class': 'accent-[#6ac2b9] w-4 h-4 cursor-pointer mr-2'
            }),
            'operator_fleet': forms.CheckboxSelectMultiple(attrs={
                'class': 'accent-[#6ac2b9] w-4 h-4 cursor-pointer mr-2'
            }),
        }