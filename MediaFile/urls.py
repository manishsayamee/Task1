from django.urls import path
from .views import upload_file, Home


urlpatterns = [
  path('', Home),
  path('file/', upload_file, name='file'),

]