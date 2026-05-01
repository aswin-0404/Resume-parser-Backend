from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    skills=models.JSONField()
    experience=models.FloatField()
    education=models.TextField(null=True,blank=True)
    current_company=models.CharField(max_length=255,null=True,blank=True)
    resume_file=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name