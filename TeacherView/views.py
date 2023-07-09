from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Experiment, Equipment, Chemicals, Steps
from .forms import ExperimentForm
from .serializers import ExperimentSerializer
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.mixins import LoginRequiredMixin 

class ExperimentCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def get(self, request):
        form = ExperimentForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = ExperimentForm(request.POST)
        if form.is_valid():
            experiment = form.save()
            equipment_names = request.POST.getlist('equipment')
            chemicals_names = request.POST.getlist('chemicals')
            steps = request.POST.getlist('steps')
            equipment_objects = [Equipment(experiment=experiment, name=name) for name in equipment_names[0].split(',') if name]
            chemicals_objects = [Chemicals(experiment=experiment, name=name) for name in chemicals_names[0].split(',') if name]
            steps = steps[0].split(';')
            # print(steps)
            steps_objects = []
            for step in steps:
                if step:
                    step = step.split(',')
                    step_object = Steps(experiment=experiment, verb=step[0], quantity=step[1] if step[1] else 0, chemical=step[2], equipment=step[3])
                    steps_objects.append(step_object)
            experiment.save()
            Equipment.objects.bulk_create(equipment_objects)
            Chemicals.objects.bulk_create(chemicals_objects)
            Steps.objects.bulk_create(steps_objects)
            return redirect('experiment_detail', pk=experiment.pk)
        return render(request, 'create.html', {'form': form})



class ExperimentDetailView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    def get(self, request, pk):
        experiment = get_object_or_404(Experiment, pk=pk)
        equipment = Equipment.objects.filter(experiment=experiment)
        chemical = Chemicals.objects.filter(experiment=experiment)
        steps = Steps.objects.filter(experiment=experiment)
        equipment_names = [e.name for e in equipment]
        chemical_names = [c.name for c in chemical]
        steps_names = [s.formatted_step for s in steps]
        return render(request, 'experiment_detail.html', {'experiment': experiment, 'equipment': equipment_names, 'chemicals': chemical_names, 'steps': steps_names})
    

class ExperimentListView(View):
    def get(self, request):
        data = request.GET
        print(data)
        exp_id = data.get('id')
        method = data.get('_method')
        print(exp_id, method)
        if method == '_delete' and exp_id:
            try:
                experiment = Experiment.objects.get(id=exp_id).delete()
            except:
                pass
        experiments = Experiment.objects.all()
        return render(request, 'experiment_list.html', {'experiments': experiments})
    
# to add swagger documentation to the API
class ApiExperimentView(generics.ListCreateAPIView):
    serializer_class = ExperimentSerializer
    queryset = Experiment.objects.all()

class ApiExperimentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperimentSerializer
    queryset = Experiment.objects.all()