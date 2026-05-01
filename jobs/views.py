from django.shortcuts import render
from .models import Job
from .serializers import JobSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class JobListView(ListAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer