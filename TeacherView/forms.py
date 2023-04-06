from django import forms
from .models import Experiment, Equipment, Chemicals,Steps

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'observation', 'conclusion']
# class ExperimentForm(forms.ModelForm):
#     equipment = forms.MultipleChoiceField(choices=Equipment.EQUIPMENT_CHOICES, widget=forms.CheckboxSelectMultiple())
#     chemicals = forms.MultipleChoiceField(choices=Chemicals.CHEMICALS_CHOICES, widget=forms.CheckboxSelectMultiple())

#     class Meta:
#         model = Experiment
#         fields = '__all__'
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name']

class ChemicalsForm(forms.ModelForm):
    class Meta:
        model = Chemicals
        fields = ['name', 'symbol']

class StepsForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = ['step']
