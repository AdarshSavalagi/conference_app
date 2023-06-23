from django.urls import path
from .views import *
urlpatterns = [
    path('',index),
    path('signin/',signin),
    path('download-photos/', issueCertificate, name='download_photos'),
]
