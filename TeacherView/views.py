from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Experiment, Equipment, Chemicals, Steps
from .forms import ExperimentForm


class ExperimentCreateView(View):
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
            steps_objects = [Steps(experiment=experiment, step=step) for step in steps[1].split(',') if step]
            experiment.save()
            Equipment.objects.bulk_create(equipment_objects)
            Chemicals.objects.bulk_create(chemicals_objects)
            Steps.objects.bulk_create(steps_objects)
            return redirect('experiment_detail', pk=experiment.pk)
        return render(request, 'create.html', {'form': form})



class ExperimentDetailView(View):
    def get(self, request, pk):
        experiment = get_object_or_404(Experiment, pk=pk)
        equipment = Equipment.objects.filter(experiment=experiment)
        chemical = Chemicals.objects.filter(experiment=experiment)
        steps = Steps.objects.filter(experiment=experiment)
        equipment_names = [e.name for e in equipment]
        chemical_names = [c.name for c in chemical]
        steps_names = [s.step for s in steps]
        return render(request, 'experiment_detail.html', {'experiment': experiment, 'equipment': equipment_names, 'chemicals': chemical_names, 'steps': steps_names})

class ExperimentListView(View):
    def get(self, request):
        experiments = Experiment.objects.all()
        return render(request, 'experiment_list.html', {'experiments': experiments})