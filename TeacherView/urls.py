from django.urls import path
from .views import ExperimentCreateView, ExperimentDetailView,ExperimentListView, ApiExperimentView, ApiExperimentDetailView, El8alyView

urlpatterns = [
    path('create/', ExperimentCreateView.as_view(), name='experiment_create'),
    path('experiment/<int:pk>/', ExperimentDetailView.as_view(), name='experiment_detail'),
    path('experiments/', ExperimentListView.as_view(), name='experiments_list'),
    path('api/Experiments/', ApiExperimentView.as_view(), name='experiments_api'),
    path('api/Experiment/<int:pk>/', ApiExperimentDetailView.as_view(), name='experiments_api_detail'),
    path('3mena/', El8alyView.as_view()),
]