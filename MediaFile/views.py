# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage

# def File_upload(request):
#   if request.method == "POST":
#     print("Post Data", request.POST)
#     print("files",  request.FILES)

#     file_obj = request.FILES['myfile']
#     print("file before save", file_obj.name)
#     fs = FileSystemStorage()
#     filename = fs.save(file_obj.name, file_obj)

#     file_url = fs.url(filename)

#     print("filename after save", filename)
#     print('File url name is', file_url)

#   return render(request, 'UploadFile/media.html')

from django.shortcuts import render
from .forms import ModelFormFileUpload
from .models import FileUpload
from django.http import HttpResponse

def upload_file(request):
  if request.method=='POST':
    
    form = ModelFormFileUpload(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponse('Thank You!!')
  else:
    form = ModelFormFileUpload()

  return render(request, 'UploadFile/media.html', {'form':form})

def Home(request):
  return render(request, 'UploadFile/home.html')