from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=300)
    code=models.CharField(max_length=20,null=True)
    skills=models.JSONField()
    experience=models.FloatField()
    location=models.CharField(max_length=300)
    description=models.TextField()

    def __str__(self):
        return self.title