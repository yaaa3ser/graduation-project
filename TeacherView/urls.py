from django.urls import path
from .views import ExperimentCreateView, ExperimentDetailView,ExperimentListView, ApiExperimentView, ApiExperimentDetailView

urlpatterns = [
    path('create/', ExperimentCreateView.as_view(), name='experiment_create'),
    path('experiment/<int:pk>/', ExperimentDetailView.as_view(), name='experiment_detail'),
    path('experiments/', ExperimentListView.as_view(), name='experiments_list'),
    path('api/experiments/', ApiExperimentView.as_view(), name='experiments_api'),
    path('api/experiment/<int:pk>/', ApiExperimentDetailView.as_view(), name='experiments_api_detail'),
]