from django.urls import path
from .views import ExperimentCreateView, ExperimentDetailView,ExperimentListView

urlpatterns = [
    path('create/', ExperimentCreateView.as_view(), name='experiment_create'),
    path('experiment/<int:pk>/', ExperimentDetailView.as_view(), name='experiment_detail'),
    path('experiments/', ExperimentListView.as_view(), name='experiments_list'),
    
]