from django.db import models

class FileUpload(models.Model):
  full_name = models.CharField(max_length=120)
  file = models.FileField()