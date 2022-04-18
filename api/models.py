from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import ImageField

# Create your models here.
class Project(models.Model):
  TRACK_SELECTION=(
    ('ANDROID', 'ANDROID'),
    ('FULLSTACK', 'FULLSTACK'),
  )
  # ProjectId = models.AutoField(primary_key=True, default=0)
  project_name=models.CharField(max_length=100)
  project_type=models.CharField(max_length=9, choices=TRACK_SELECTION, default=0)
  project_landingpage=CloudinaryField('media')
  project_description=models.TextField()
  project_owner=models.CharField(max_length=100)
  project_member1=models.CharField(max_length=50, null=True, blank=True)
  project_member2=models.CharField(max_length=50, null=True, blank=True)
  project_member3=models.CharField(max_length=50, null=True, blank=True)
  project_member4=models.CharField(max_length=50, null=True, blank=True)
  project_member5=models.CharField(max_length=50, null=True, blank=True)
  project_member6=models.CharField(max_length=50, null=True, blank=True)
  github_link=models.URLField(max_length=100)


  def __str__(self) -> str:
    return self.project_name