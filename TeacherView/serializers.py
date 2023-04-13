from rest_framework import serializers
from .models import Experiment, Equipment, Chemicals, Steps

class EquipmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Equipment
        fields = ['name',]

class ChemicalsSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Equipment
        fields = ['name',]

class StepsSerializer(serializers.ModelSerializer):
    step = serializers.CharField()
    class Meta:
        model = Equipment
        fields = ['step',]
class ExperimentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    equipments = EquipmentSerializer(many=True)
    chemicals = ChemicalsSerializer(many=True)
    steps = StepsSerializer(many=True)
    observation = serializers.CharField()
    conclusion = serializers.CharField()
    class Meta:
        model = Experiment
        fields = '__all__'
        

