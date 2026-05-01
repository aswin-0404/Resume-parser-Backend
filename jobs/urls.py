from django.urls import path
from .views import JobListView

urlpatterns = [
    path('list-jobs/',JobListView.as_view()),
    
]
