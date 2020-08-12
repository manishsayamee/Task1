from .models import FileUpload
from django.forms import ModelForm


class ModelFormFileUpload(ModelForm):
  class Meta:
    model = FileUpload
    fields = ['full_name', 'file']
