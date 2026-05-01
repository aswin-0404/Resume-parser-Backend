from django.urls import path
from .views import CandidateListView,ParseResumeView,MatchView,ResumeUploadView

urlpatterns = [
    path('all-candidates/',CandidateListView.as_view()),
    path('upload-resume/',ResumeUploadView.as_view()),
    path('parse-resume/<int:pk>/',ParseResumeView.as_view()),
    path('match-job/',MatchView.as_view())
]
