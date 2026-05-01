from django.shortcuts import render
from rest_framework.views import APIView
from .models import Candidate
from rest_framework.response import Response

from .utils import extract_text
from .resume_parser import parse_resume_simple

from jobs.models import Job
from .utils import match_candidate_job

from rest_framework.generics import ListAPIView
from .serializers import CandidateSerializer

# Create your views here.
class ResumeUploadView(APIView):
    def post(self,request):
        file=request.FILES.get('resume')

        candidate=Candidate.objects.create(
            resume_file=file,
            name="temp",
            email="temp@gmail.com",
            phone="2145854759",
            skills=[],
            experience=0
        )

        return Response({
            "candidate_id":candidate.id,
            "file_url": candidate.resume_file.url
        })
    
class ParseResumeView(APIView):
    def post(self,request,pk):
        candidate=Candidate.objects.get(id=pk)

        file_path= candidate.resume_file.path
        text=extract_text(file_path)

        parsed_data=parse_resume_simple(text)

        print(parsed_data)

        candidate.name = parsed_data.get("name", "")
        candidate.email = parsed_data.get("email", "")
        candidate.phone = parsed_data.get("phone", "")
        candidate.skills = parsed_data.get("skills", [])
        candidate.experience = parsed_data.get("experience", 0)
        candidate.education = parsed_data.get("education", "")
        candidate.current_company = parsed_data.get("current_company", "")

        candidate.save()

        return Response(parsed_data)


class MatchView(APIView):
    def post(self,request):
        candidate_id=request.data.get("candidate_id")
        job_id=request.data.get("job_id")

        candidate= Candidate.objects.get(id=candidate_id)
        job=Job.objects.get(id=job_id)

        result=match_candidate_job(candidate,job)

        return Response(result)


class CandidateListView(ListAPIView):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer
