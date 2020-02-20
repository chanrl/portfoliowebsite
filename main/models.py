from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_content = models.TextField()
    project_published = models.DateTimeField("date published", default=timezone.now())
    project_image = models.CharField(max_length=200)
    
    project_url = models.URLField()

    def __str__(self):
        return self.project_title