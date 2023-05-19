from django import forms
from .models import Experiment, Equipment, Chemicals,Steps

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'observation', 'conclusion']
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name']

class ChemicalsForm(forms.ModelForm):
    class Meta:
        model = Chemicals
        fields = ['name', 'symbol']
